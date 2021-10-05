#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup

# Package meta-data.
NAME = '{{cookiecutter.project_slug}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
URL = 'https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}'
EMAIL = '{{cookiecutter.email}}'
AUTHOR = '{{cookiecutter.author}}'
REQUIRES_PYTHON = '>=3.6.0'
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

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=['{{cookiecutter.project_slug}}'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ])
