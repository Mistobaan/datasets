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
"""`tfds.features.FeatureConnector` API defining feature types."""

from tfds.features import text

from tfds.features.audio_feature import Audio
from tfds.features.bounding_boxes import BBox
from tfds.features.bounding_boxes import BBoxFeature
from tfds.features.class_label_feature import ClassLabel
from tfds.features.feature import FeatureConnector
from tfds.features.feature import Tensor
from tfds.features.feature import TensorInfo
from tfds.features.features_dict import FeaturesDict
from tfds.features.image_feature import Image
from tfds.features.sequence_feature import Sequence
from tfds.features.text_feature import Text
from tfds.features.translation_feature import Translation
from tfds.features.translation_feature import TranslationVariableLanguages
from tfds.features.video_feature import Video

__all__ = [
    "text",
    "Audio",
    "BBox",
    "BBoxFeature",
    "ClassLabel",
    "FeatureConnector",
    "FeaturesDict",
    "Tensor",
    "TensorInfo",
    "Sequence",
    "Image",
    "Text",
    "Video",
]
