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
"""`tfds.download.DownloadManager` API."""

from tfds.download.checksums import add_checksums_dir
from tfds.download.download_manager import DownloadConfig
from tfds.download.download_manager import DownloadManager
from tfds.download.downloader import DownloadError
from tfds.download.extractor import iter_archive
from tfds.download.resource import ExtractMethod
from tfds.download.resource import Resource
from tfds.download.util import ComputeStatsMode
from tfds.download.util import GenerateMode

__all__ = [
    "add_checksums_dir",
    "DownloadConfig",
    "DownloadManager",
    "DownloadError",
    "ComputeStatsMode",
    "GenerateMode",
    "Resource",
    "ExtractMethod",
    "iter_archive",
]
