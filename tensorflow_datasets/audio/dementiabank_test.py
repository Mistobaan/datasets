
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
"""Tests for DementiaBank dataset."""



from tensorflow_datasets import testing
from tensorflow_datasets.audio import dementiabank


class DementiabankTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = dementiabank.Dementiabank
  SPLITS = {
      'train': 3,
      'validation': 1,
      'test': 1,
  }


if __name__ == '__main__':
  testing.test_main()
