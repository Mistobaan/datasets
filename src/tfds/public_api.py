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
from tfds import folder_dataset
from tfds import download
from tfds import decode
from tfds import features
from tfds import units
from tfds import visualization
from tfds.folder_dataset import ImageFolder
from tfds.folder_dataset import TranslateFolder
from tfds.dataset_utils import as_numpy
from tfds.download import GenerateMode
from tfds.registered import builder
from tfds.registered import builder_cls
from tfds.registered import list_builders
from tfds.registered import load
from tfds.registered import skip_registration
from tfds.splits import Split
from tfds.utils.gcs_utils import is_dataset_on_gcs
from tfds.utils.read_config import ReadConfig
from tfds.utils.tqdm_utils import disable_progress_bar
from tfds.visualization import show_examples
from tfds.visualization import show_statistics
from tfds.version import __version__
from tfds.dataset_builder import GeneratorBasedBuilder, BuilderConfig, BeamBasedBuilder
from tfds.utils.version import Version
from tfds.dataset_info import DatasetInfo
from tfds.splits import SplitGenerator, SplitInfo
from tfds.lazy_imports_lib import lazy_imports
from tfds.api_utils import disallow_positional_args

with skip_registration():
    # We import testing namespace but without registering the tests datasets
    # (e.g. DummyMnist,...).
    from tfds import testing


__all__ = [
    "as_numpy",
    "folder_dataset",
    "builder",
    "builder_cls",
    "decode",
    "disable_progress_bar",
    "download",
    "features",
    "GeneratorBasedBuilder",
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
    "Version",
    "DatasetInfo",
    "SplitGenerator",
    "SplitInfo",
    "lazy_imports",
    "BuilderConfig",
    "BeamBasedBuilder",
    "__version__",
    "disallow_positional_args",
]
