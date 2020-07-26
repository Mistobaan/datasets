
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
"""Tests for LostAndFound dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import lost_and_found


class LostAndFoundTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = lost_and_found.LostAndFound
  BUILDER_CONFIG_NAMES_TO_TEST = ['semantic_segmentation', 'full']
  SPLITS = {
      'train': 4,  # Number of fake train example
      'test': 2,  # Number of fake test example
  }
  # files as generated by fake data functions in testing/lost_and_found.py
  DL_EXTRACT_RESULT = {
      'image_left': 'leftImg8bit.zip',
      'image_right': 'rightImg8bit.zip',
      'disparity_map': 'disparity.zip',
      'segmentation_label': 'gtCoarse.zip',
      'instance_id': 'gtCoarse.zip'
  }


if __name__ == '__main__':
  testing.test_main()
