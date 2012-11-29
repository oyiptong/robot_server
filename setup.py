# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from setuptools import setup

requires = [
        'tornado==2.4.1',
]

setup(name="robots.server",
      version="1.0",
      description="API server for robot",
      url="",
      author="robots",
      author_email="robots",
      packages=['robots', 'robots.server'],
      namespace_packages=['robots'],
      include_package_data=True,
      install_requires = requires,
      scripts=['scripts/robot-server']
)
