# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""


class PyValitronError(Exception):
    def __init__(self, error_info):
        Exception.__init__(self, "PyValitron exception was raised")
        self.error_info = error_info