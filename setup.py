# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
from pyvalitron import __version__
from pyvalitron import read_file


setup(
    name = "pyvalitron",
    version = __version__,
    author = "Clivern",
    author_email = "hello@clivern.com",
    description="Python Inputs Validation Library",
    license = "MIT",
    keywords = "validation,forms,inputs",
    url = "http://clivern.github.io/pyvalitron/",
    packages = ['pyvalitron'],
    long_description = read_file('README.md'),
    classifiers = [
        'Classifier: Development Status :: 3 - Alpha',
        'Classifier: License :: OSI Approved :: MIT License',
        'Classifier: Programming Language :: Python :: 2.7',
        'Classifier: Programming Language :: Python :: 3.0',
        'Classifier: Programming Language :: Python :: 3.1',
        'Classifier: Programming Language :: Python :: 3.2',
        'Classifier: Programming Language :: Python :: 3.3',
        'Classifier: Programming Language :: Python :: 3.4',
        'Classifier: Programming Language :: Python :: 3.5',
        'Classifier: Topic :: Utilities'
    ],
)