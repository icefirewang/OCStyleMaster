#!/usr/bin/env python
# Copyright 2013 The OCStyleMaster Authors.
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

"""Setup script for OCStyleMaster."""
import sys

try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup

PACKAGES=find_packages("./src/",exclude=[])
print(PACKAGES)

setup(name='ocstylemaster',
      version='0.2.3',
      description='Objective-C style checker',
      keywords=('pip','Objective-C','OC','style'),
      author='icefire_wang, Inc.',
      author_email = "icefire_wang@163.com",
      # url="./",
      url='https://github.com/icefirewang/OCStyleMaster',
      package_dir={'': "src"},
        # packages =[ "OCStyleMaster",
        #             "OCStyleMaster.common",
        #             "OCStyleMaster.config",
        #             "OCStyleMaster.managers",
        #             "OCStyleMaster.models",
        #             "OCStyleMaster.models.blocks",
        #             "OCStyleMaster.models.common",
        #             "OCStyleMaster.models.error",
        #             "OCStyleMaster.tools",
        #             "OCStyleMaster.utils"],
      packages=PACKAGES,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'occ = OCStyleMaster.main:main'
          ]
      },
)