# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""
import cgi
from .validator import Validator
from .sanitizer import Sanitizer
from .utils import Utils
from .exceptions import PyValitronError


{
    'input' : {
        'validate': {
            'required': [],
            'length_between': [5, 3]
        }
        'sanitize':{

        }
    }
}


class Form(object):

    _form = None
    _inputs = {}
    _errors = {}
    _sinputs = {}

    _validator = None
    _sanitizer = None
    _utils = None

    def __init__(self, inputs):
        self._form = cgi.FieldStorage()
        self._inputs = inputs
        self._validator = Validator()
        self._sanitizer = Sanitizer()
        self._utils = Utils()

    def get_inputs(self):
        return self._inputs

    def get_sinputs(self):
        return self._sinputs

    def get_errors(self):
        return self._errors

    def validate(self):
        for current_input, validation_rule in self._inputs.iteritems():
            self._validator.set_input(self._form.getfirst(current_input, ''))

    def sanitize(self):
        pass
