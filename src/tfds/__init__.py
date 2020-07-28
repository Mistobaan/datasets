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
# pylint: disable=line-too-long
"""`tfds` (`tfds`) defines a collection of datasets ready-to-use with TensorFlow.

Each dataset is defined as a `tfds.DatasetBuilder`, which encapsulates
the logic to download the dataset and construct an input pipeline, as well as
contains the dataset documentation (version, splits, number of examples, etc.).

The main library entrypoints are:

* `tfds.builder`: fetch a `tfds.DatasetBuilder` by name
* `tfds.load`: convenience method to construct a builder, download the data, and
  create an input pipeline, returning a `tf.data.Dataset`.

Documentation:

* These API docs
* [Available datasets](https://www.tensorflow.org/datasets/catalog/overview)
* [Colab tutorial](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb)
* [Add a dataset](https://www.tensorflow.org/datasets/add_dataset)
"""

# Public API to create and generate a dataset
from tfds.public_api import *  # pylint: disable=wildcard-import

# __all__ for import * as well as documentation
from tfds import public_api  # pylint: disable=g-bad-import-order

__all__ = public_api.__all__