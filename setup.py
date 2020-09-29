#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about = {}
with open(path.join(here, 'pip_update', '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name='pip-update',

    version=about['__version__'],

    description='Pip Update',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/albertyw/pip-update',

    author='Albert Wang',
    author_email='git@albertyw.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Version Control',

         'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='',

    package_data={"pip_update": ["py.typed"]},
    packages=find_packages(exclude=["tests"]),

    py_modules=["pip_update.pip_update"],

    install_requires=[],

    test_suite="pip_update.tests",

    # testing requires flake8 and coverage but they're listed separately
    # because they need to wrap setup.py
    extras_require={
        'dev': [],
        'test': [],
    },

    entry_points={
        'console_scripts': [
            'pip_update=pip_update.pip_update:main',
        ],
    },
)
