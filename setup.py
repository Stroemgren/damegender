#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import os
import re
from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

cwd = os.getcwd()

def files_one_level(directory):
    f = os.popen('find '+ directory )
    l = []
    for line in f:
        fields = line.strip().split()
        l.append(fields[0])
    return l

def files_one_level_drop_pwd(directory):
    f = os.popen('find '+ directory)
    l = []
    for line in f:
        fields = line.strip().split()
        if not(os.path.isdir(fields[0])) and ("__init__.py" not in fields[0]):
            l.append(drop_pwd(fields[0]))
    return l

def drop_pwd(s):
    cwd = os.getcwd()
    result = ""
    if re.search(cwd, s):
        result = re.sub(cwd+'/', '', s)
    return result

setup(name='damegender',
      python_requires='>3.6',
      version='0.5.3.pre3',
      description='Gender Detection Tool by David Arroyo MEnéndez',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
      ],
      keywords='gender, repositories',
      url='http://github.com/davidam/damegender',
      author='David Arroyo Menéndez',
      author_email='davidam@gmail.com',
      license='GPLv3',
      packages=['damegender', 'damegender.app', 'damegender.test', 'damegender.files'],
      package_dir={'damegender': 'src/damegender', 'damegender.app': 'src/damegender/app', 'damegender.test': 'src/damegender/test', 'damegender.names': 'src/damegender/files/names', 'damegender.datamodels': 'src/damegender/files/datamodels', 'damegender.inesurnames': 'src/damegender/files/inesurnames', 'damegender.images': 'src/damegender/files/images', 'damegender.root': '.'},
      package_data={'damegender': ['*'],
                    'damegender.app': ['*'],
                    'damegender.test': ['*'],
                    'damegender.names': ['*'],
                    'damegender.datamodels': ['*'],
                    'damegender.root': ['*']},
      data_files=[('damegender', ['src/damegender/GPL.txt', 'src/damegender/README.md', 'src/damegender/config.cfg', 'src/damegender/config.enabled.cfg', 'src/damegender/files/features_list.csv', 'src/damegender/files/features_list_cat.csv', 'src/damegender/files/features_list_no_cat.csv', 'src/damegender/files/features_list_no_undefined.csv', 'src/damegender/files/scientifics.txt', 'src/damegender/files/pca.json', 'src/damegender/files/gnu-maintainers.csv', 'src/damegender/files/forbes2020.csv', 'src/damegender/files/logs/grep.tmp'] + files_one_level_drop_pwd(cwd+"/src/damegender/files/datamodels") + files_one_level_drop_pwd(cwd+"/src/damegender/files/images") + files_one_level_drop_pwd(cwd+"/src/damegender/files/mbox") + files_one_level_drop_pwd(cwd+"/src/damegender/files/names") + files_one_level_drop_pwd(cwd+"/src/damegender/files/inesurnames") + files_one_level_drop_pwd(cwd+"/src/damegender/files/tests") + files_one_level_drop_pwd(cwd+"/src/damegender/sh/languages") + files_one_level_drop_pwd(cwd+"/src/damegender/sh/logs") + files_one_level_drop_pwd(cwd+"/src/damegender/sh/regenerate") + files_one_level_drop_pwd(cwd+"/src/damegender/sh/tests"))],
      install_requires=[
          'markdown',
          'nltk',
          'requests',
          'numpy',
          'scipy',
          'scikit-learn',
          'unidecode',
          'pandas',
          'matplotlib',
          'json2html'
      ],
      extras_require = {
          'mails_and_repositories' : ["perceval"],
          'apis': ["genderize"],
          'all' : ["perceval", "genderize"],
          'all_extended' : ["perceval", "gender_guesser", "genderize", "newspaper3k", "transliterate"]
      },
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['main=main.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
