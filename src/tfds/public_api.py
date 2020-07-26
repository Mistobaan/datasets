# coding=utf-8
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
"""Public API of tfds, without the registered dataset."""

# pylint: disable=unused-import,g-import-not-at-top,g-bad-import-order,wrong-import-position
from tfds.core import tf_compat
tf_compat.ensure_tf_install()

from tfds import core
from tfds.core import folder_dataset
from tfds.core import download
from tfds.core import decode
from tfds.core import features
from tfds.core import units
from tfds.core import visualization
from tfds.core.folder_dataset import ImageFolder
from tfds.core.folder_dataset import TranslateFolder
from tfds.core.dataset_utils import as_numpy
from tfds.core.download import GenerateMode
from tfds.core.registered import builder
from tfds.core.registered import builder_cls
from tfds.core.registered import list_builders
from tfds.core.registered import load
from tfds.core.splits import Split
from tfds.core.utils.gcs_utils import is_dataset_on_gcs
from tfds.core.utils.read_config import ReadConfig
from tfds.core.utils.tqdm_utils import disable_progress_bar
from tfds.core.visualization import show_examples
from tfds.core.visualization import show_statistics
from tfds.version import __version__

with core.registered.skip_registration():
  # We import testing namespace but without registering the tests datasets
  # (e.g. DummyMnist,...).
  from tfds import testing


__all__ = [
    "as_numpy",
    "core",
    "folder_dataset",
    "builder",
    "builder_cls",
    "decode",
    "disable_progress_bar",
    "download",
    "features",
    "GenerateMode",
    "ImageFolder",
    "is_dataset_on_gcs",
    "list_builders",
    "load",
    "ReadConfig",
    "Split",
    "show_examples",
    "show_statistics",
    "testing",
    "TranslateFolder",
    "units",
    "visualization",
    "__version__",
]
