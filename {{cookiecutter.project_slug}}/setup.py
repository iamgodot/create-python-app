#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = '{{cookiecutter.project_slug}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
URL = 'https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}'
EMAIL = '{{cookiecutter.email}}'
AUTHOR = '{{cookiecutter.author}}'
REQUIRES_PYTHON = '>=3.6, <4'
VERSION = None

REQUIRED = []

here = os.path.abspath(os.path.dirname(__file__))

# Load the package's __version__.py module as a dictionary.
about = {}

if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Get the long description from README.md
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests', )),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['{{cookiecutter.project_slug}}'],

    # entry_points={
    #     'console_scripts': ['cmd=package.module:main'],
    # },
    install_requires=REQUIRED,
    extras_require={
        'dev': ['pytest', 'flake8'],
    },
    include_package_data=True,
    # Specify files to be included in the package
    # package_data={'': []}
    exclude_package_data={'': []},
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ])
