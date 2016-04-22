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
    name="pyvalitron",
    version=__version__,
    author="Clivern",
    author_email="hello@clivern.com",
    description="Python Inputs Validation Library",
    license="MIT",
    keywords="validation,forms,inputs",
    url="http://clivern.github.io/pyvalitron/",
    packages=['pyvalitron'],
    long_description=read_file('README.md'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
    ],
)
