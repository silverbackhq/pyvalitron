# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

class Form(object):

    _inputs = {}
    _errors = {}
    _sinputs = {}

    _validator = None
    _sanitizer = None
    _utils = None

    def __init__(self, inputs):
        self._inputs = inputs
        self._validator = None
        self._sanitizer = None
        self._utils = None

    def get_inputs(self):
        return self._inputs

    def get_sinputs(self):
        return self._sinputs

    def get_errors(self):
        return self._errors

    def validate(self):
        pass

    def sanitize(self):
        pass
