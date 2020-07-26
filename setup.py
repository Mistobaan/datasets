# Lint as: python3
"""tensorflow/datasets is a library of datasets ready to use with TensorFlow.

tensorflow/datasets is a library of public datasets ready to use with
TensorFlow. Each dataset definition contains the logic necessary to download and
prepare the dataset, as well as to read it into a model using the
`tf.data.Dataset` API.

Usage outside of TensorFlow is also supported.

See the README on GitHub for further documentation.
"""

import datetime
import itertools
import os
import sys

from setuptools import find_packages
from setuptools import setup

__version__ = '0.1.0'

nightly = False
if '--nightly' in sys.argv:
  nightly = True
  sys.argv.remove('--nightly')

project_name = 'tfds'

if nightly:
  project_name = 'tfds-nightly'
  datestring = (os.environ.get('TFDS_NIGHTLY_TIMESTAMP') or
                datetime.datetime.now().strftime('%Y%m%d%H%M'))
  __version__ += 'dev%s' % datestring

DOCLINES = __doc__.split('\n')

REQUIRED_PKGS = [
    'absl-py==0.8.0',
    'tensorflow>=1.15.3,<2.0',
    'tensorflow-metadata',
    # 'attrs>=18.1.0',
    # 'future',
    # 'numpy', # this should be tensorflow's deps
    'promise', # these should be removed with async/await #TODO
    'protobuf>=3.6.1',
    'requests>=2.19.0',
    'six', # we can't unsix ..
    # 'termcolor',
    'tqdm',
    # 'wrapt',
]

TESTS_REQUIRE = [
    # 'jupyter',
    # 'mako',
    'dill>=0.3.1.1,<0.3.2',  # TODO(tfds): move to TESTS_REQUIRE.
    'pytest>=4.4.0',
    'pytest-xdist==1.33.0',
    'tensorflow-data-validation',
    # TODO(b/142892342): Re-enable
    # 'tensorflow-docs @ git+https://github.com/tensorflow/docs#egg=tensorflow-docs',  # pylint: disable=line-too-long
]

# Static files needed by datasets.
DATASET_FILES = [
]

# Extra dependencies required by specific datasets
DATASET_EXTRAS = {
}

EXTRAS_REQUIRE = {
    'matplotlib': ['matplotlib'],
    'tensorflow-data-validation': ['tensorflow-data-validation'],

    # Tests dependencies are installed in ./oss_scripts/oss_pip_install.sh
    # and run in ./oss_scripts/oss_tests.sh
    'tests': TESTS_REQUIRE,
}
EXTRAS_REQUIRE.update(DATASET_EXTRAS)

setup(
    name=project_name,
    version=__version__,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.',
    author_email='packages@tensorflow.org',
    url='https://github.com/tensorflow/datasets',
    download_url='https://github.com/tensorflow/datasets/tags',
    license='Apache 2.0',
    #packages=[find_packages('src/tfds')],
    package_data={
        # 'tensorflow_datasets': DATASET_FILES + [
        #     'scripts/documentation/templates/*',
        # ],
    },
    scripts=[],
    install_requires=REQUIRED_PKGS,
    python_requires='>=3.6',
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow machine learning datasets',
)
