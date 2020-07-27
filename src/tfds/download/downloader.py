# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Async download API with checksum verification. No business logic."""


import concurrent.futures
import contextlib
import functools
import hashlib
import io
import os
import re
from typing import Any, ContextManager, Iterable, Iterator, Tuple, Union
import promise
import requests

from six.moves import urllib
import tensorflow.compat.v2 as tf
from tfds import units
from tfds import utils
from tfds.download import checksums as checksums_lib
from tfds.download import resource as resource_lib

from absl import logging

_DRIVE_URL = re.compile(r"^https://drive\.google\.com/")


# Response interface. Has `.url` and `.headers` attribute
Response = Union[requests.Response, urllib.response.addinfourl]


@utils.memoize()
def get_downloader(*args: Any, **kwargs: Any) -> "_Downloader":
    return _Downloader(*args, **kwargs)


def _get_filename(response: Response) -> str:
    content_disposition = response.headers.get("content-disposition", None)
    if content_disposition:
        match = re.findall('filename="(.+?)"', content_disposition)
        if match:
            return match[0]
    return utils.basename_from_url(response.url)


class DownloadError(Exception):
    pass


class _Downloader(object):
    """
    Class providing async download API with checksum validation.

    NOTE: Do not instantiate this class directly. Instead, call `get_downloader()`.
    """

    def __init__(self, max_simultaneous_downloads: int = 50, checksumer=None):
        """
        Init _Downloader instance.

        Args:
            max_simultaneous_downloads: `int`, max number of simultaneous downloads.
            checksumer: `hashlib.HASH`. Defaults to `hashlib.sha256`.
        """
        self._executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=max_simultaneous_downloads
        )
        self._checksumer_cls = checksumer or hashlib.sha256
        self._pbar_url = None
        self._pbar_dl_size = None

    @contextlib.contextmanager
    def tqdm(self) -> Iterator[None]:
        """Add a progression bar for the current download."""
        async_tqdm = utils.async_tqdm
        with async_tqdm(total=0, desc="Download Completed...", unit=" url") as pbar_url:
            with async_tqdm(total=0, desc="Download Size...", unit=" MiB") as pbar_dl_size:
                self._pbar_url = pbar_url
                self._pbar_dl_size = pbar_dl_size
                yield

    def download(self, resource: "Resource", destination_path: str):
        """
        Download url to given path.

        Returns Promise -> sha256 of downloaded file.

        Args:
            url: address of resource to download.
            destination_path: `str`, path to directory where to download the resource.

        Returns:
            Promise obj -> (`str`, int): (downloaded object checksum, size in bytes).
        """
        self._pbar_url.update_total(1)
        future = self._executor.submit(self._sync_download, resource, destination_path)
        return promise.Promise.resolve(future)

    def _sync_file_copy(
        self, resource: resource_lib.Resource, destination_path: str
    ) -> resource_lib.Resource:
        out_path = os.path.join(destination_path, os.path.basename(resource.url))
        def _check_progress():
            remote_stats = tf.io.gfile.stats(resource.url)
            while True:
                self._pbar_dl_size.update_total(1000)
                local_stats = tf.io.gfile.stats(out_path)
                print(local_stats, remote_stats)
                self._pba
                import time
                time.sleep(1000)

        future = self._executor.submit(_check_progress)
        tf.io.gfile.copy(resource.url, out_path)
        hexdigest, size = utils.read_checksum_digest(
            out_path, checksum_cls=self._checksumer_cls
        )
        url_hexdigest = resource.url_checksum.split(':')[-1] 
        if url_hexdigest != hexdigest:
            raise DownloadError("checksum: %s != %s" % (url_hexdigest, hexdigest))
        
        self._pbar_dl_size.update_total(size)
        self._pbar_dl_size.update(size)

        return resource_lib.Resource(
            url=resource.url,
            url_checksum=url_hexdigest,
            local_path=out_path,
            local_path_info=checksums_lib.UrlInfo(checksum=hexdigest, size=size)
        )

    def _sync_download(self, resource: resource_lib.Resource, destination_path: str) -> resource_lib.Resource:
        """
        Synchronous version of `download` method.

        To download through a proxy, the `HTTP_PROXY`, `HTTPS_PROXY`,
        `REQUESTS_CA_BUNDLE`,... environement variables can be exported, as
        described in:
        https://requests.readthedocs.io/en/master/user/advanced/#proxies

        Args:
            url: url to download
            destination_path: path where to write it

        Returns:
            None

        Raises:
            DownloadError: when download fails.
        """
        try:
            # If url is on a filesystem that gfile understands, use copy. Otherwise,
            # use requests (http) or urllib (ftp).
            if not resource.url.startswith("http"):
                return self._sync_file_copy(resource, destination_path)
        except tf.errors.UnimplementedError:
            logging.info('could not handle file %s' % resource.url)
            pass
        # except Exception as exc:
        #     logging.info('could not handle file %s' % resource.url)
        #     return

        with _open_url(resource.url) as (response, iter_content):
            fname = _get_filename(response)
            path = os.path.join(destination_path, fname)
            size = 0

            # Initialize the download size progress bar
            size_mb = 0
            unit_mb = units.MiB
            total_size = int(response.headers.get("Content-length", 0)) // unit_mb
            self._pbar_dl_size.update_total(total_size)
            with tf.io.gfile.GFile(path, "wb") as file_:
                checksum = self._checksumer_cls()
                for block in iter_content:
                    size += len(block)
                    checksum.update(block)
                    file_.write(block)

                    # Update the download size progress bar
                    size_mb += len(block)
                    if size_mb > unit_mb:
                        self._pbar_dl_size.update(size_mb // unit_mb)
                        size_mb %= unit_mb
        self._pbar_url.update(1)
        checksum_digest = checksum.hexdigest() 
        if resource.url_checksum != checksum_digest:
            raise DownloadError('checksum mismatch: %s!=%s file:%s' % (resource.url_checksum, checksum_digest, path))

        return resource_lib.Resource(
            url=url, 
            local_path=path,
            local_path_info=checksums_lib.UrlInfo(checksum=checksum_digest, size=size)
        )


def _open_url(url: str) -> ContextManager[Tuple[Response, Iterable[bytes]]]:
    """
    Context manager to open an url.

    Args:
        url: The url to open

    Returns:
        response: The url response with `.url` and `.header` attributes.
        iter_content: A `bytes` iterator which yield the content.
    """
    # Download FTP urls with `urllib`, otherwise use `requests`
    if url.startswith('gs'):
        open_fn = tf.io.gfile.GFile
    else:
        open_fn = _open_with_urllib if url.startswith("ftp") else _open_with_requests
    return open_fn(url)


@contextlib.contextmanager
def _open_with_requests(url: str) -> Iterator[Tuple[Response, Iterable[bytes]]]:
    with requests.Session() as session:
        if _DRIVE_URL.match(url):
            url = _get_drive_url(url, session)
        with session.get(url, stream=True) as response:
            _assert_status(response)
            yield (response, response.iter_content(chunk_size=io.DEFAULT_BUFFER_SIZE))


@contextlib.contextmanager
def _open_with_urllib(url: str) -> Iterator[Tuple[Response, Iterable[bytes]]]:
    with urllib.request.urlopen(url) as response:  # pytype: disable=attribute-error
        yield (
            response,
            iter(functools.partial(response.read, io.DEFAULT_BUFFER_SIZE), b""),
        )

@contextlib.contextmanager
def _open_with_gfile(url: str) -> Iterator[Tuple[Response, Iterable[bytes]]]:
    with tf.io.gfile.GFile(url) as gcs_fd:  # pytype: disable=attribute-error
        yield (
            gcs_fd,
            iter(functools.partial(gcs_fd.read, io.DEFAULT_BUFFER_SIZE), b""),
        )


def _get_drive_url(url: str, session: requests.Session) -> str:
    """Returns url, possibly with confirmation token."""
    with session.get(url, stream=True) as response:
        _assert_status(response)
        for k, v in response.cookies.items():
            if k.startswith("download_warning"):
                return url + "&confirm=" + v  # v is the confirm token
    # No token found, let's try with original URL:
    return url


def _assert_status(response: requests.Response) -> None:
    """Ensure the URL response is 200."""
    if response.status_code != 200:
        raise DownloadError(
            "Failed to get url {}. HTTP code: {}.".format(
                response.url, response.status_code
            )
        )
