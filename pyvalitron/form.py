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


# {
#     'input' : {
#         'validate': {
#             'required': {},
#             'length_between': {
#                    'param' : [],
#                    'error': 'Please lenght must be between '
#                }
#         }
#         'sanitize':{

#         }
#     }
# }


class Form(object):

    _form = None
    _inputs = {}
    _errors = {}
    _sinputs = {}

    _status = False

    _validator = None
    _sanitizer = None
    _utils = None

    def __init__(self, inputs):
        """Init Form Module"""
        self._form = cgi.FieldStorage()
        self._inputs = inputs
        self._validator = Validator()
        self._sanitizer = Sanitizer()
        self._utils = Utils()

    def get_inputs(self):
        """Get Original Inputs Values"""
        return self._inputs

    def get_sinputs(self):
        """Get Sanitized Inputs Values"""
        return self._sinputs

    def get_errors(self):
        """Get All Errors"""
        return self._errors

    def get_status(self):
        """Get Overall Status"""
        return self._status

    def validate(self):
        """Validate, Set Errors and Return Overall Status"""
        for current_input, validation_rule in self._inputs.iteritems():
            self._inputs[current_input]['value'] = self._form.getfirst(current_input, '')
            self._validator.set_input(self._inputs[current_input]['value'])
            status = True
            for rule_name, rule_args in validation_rule['validate'].iteritems()
                current_status = getattr(self._validator, rule_name)(*rule_args['param'])
                self._inputs[current_input]['status'] = current_status
                status &= current_status
                if not current_status:
                    self._errors[current_input] = rule_args['error']

            self._status = status
            return status

    def sanitize(self):
        """Sanitize Inputs and Store Them"""
        pass
