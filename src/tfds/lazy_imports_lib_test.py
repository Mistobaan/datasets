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
"""Tests for tfds.core.lazy_imports."""



from absl.testing import parameterized
import six
import tfds as tfds
from tfds import testing


class LazyImportsTest(testing.TestCase, parameterized.TestCase):

  # The following deps are not in the test list because the datasets that
  # require them need to have their tests run in isolation:
  # * crepe (NSynth)
  # * librosa (NSynth)
  @parameterized.parameters(
      "cv2",
      "langdetect",
      "matplotlib",
      "mwparserfromhell",
      "nltk",
      "os",
      "pandas",
      "pretty_midi",
      "pydub",
      "scipy",
      "skimage",
      "tldextract",
  )
  def test_import(self, module_name):
    if module_name == "nltk" and six.PY2:  # sklearn do not support Python2
      return
    # TODO(rsepassi): Re-enable skimage on Py3 (b/129964829)
    if module_name == "skimage" and six.PY3:
      return
    getattr(tfds.core.lazy_imports, module_name)

  def test_bad_import(self):
    with self.assertRaisesWithPredicateMatch(ImportError, "extras_require"):
      _ = tfds.core.lazy_imports.test_foo


if __name__ == "__main__":
  testing.test_main()
