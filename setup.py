#!/bin/env python

import os
from distutils.core import setup

name = 'libcloudfs'
version = '0.1'
release = '1'
versrel = version + '-' + release
readme = os.path.join(os.path.dirname(__file__), 'README.rst')
download_urlQ = 'https://github.com/downloads/btimby/fs-libcloud' \
                           '/' + name + '-' + versrel + '.tar.gz'
long_description = file(readme).read()

setup(
    name = name,
    version = versrel,
    description = 'A pyFilesystem backend for libcloud.',
    long_description = long_description,
    requires = [
        'fs',
        'dropbox',
    ],
    author = 'Ben Timby',
    author_email = 'btimby@gmail.com',
    maintainer = 'Ben Timby',
    maintainer_email = 'btimby@gmail.com',
    url = 'http://github.com/btimby/fs-libcloud/',
    download_url = download_url,
    license = 'GPLv3',
    py_modules=['dropboxfs'],
    package_data={'': ['README.rst']},
    classifiers = (
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
