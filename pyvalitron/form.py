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

    _type = 'form'
    _form = None
    _inputs = {}
    _errors = {}
    _sinputs = {}

    _vstatus = False
    _sstatus = False

    _validator = None
    _sanitizer = None
    _utils = None

    def __init__(self, inputs, inputs_type='form'):
        """Init Form Module"""
        self._type = inputs_type
        if self._type == 'form':
            self._form = cgi.FieldStorage()
        self._inputs = inputs
        self._validator = Validator()
        self._sanitizer = Sanitizer()
        self._utils = Utils()

    def get_inputs(self):
        """Get Original Inputs Values"""
        return self._inputs

    def get_errors(self):
        """Get All Errors"""
        return self._errors

    def get_vstatus(self):
        """Get Overall Sanitization Status"""
        return self._vstatus

    def get_sstatus(self):
        """Get Overall Sanitization Status"""
        return self._sstatus

    def validate(self):
        """Validate, Set Errors and Return Overall Status"""
        for current_input, validation_rule in self._inputs.iteritems():
            # Push input value to validator
            if self._type == 'form':
                self._inputs[current_input]['value'] = self._form.getfirst(current_input, '')
            self._validator.set_input(self._inputs[current_input]['value'])

            # Validate current input value
            status = True
            if 'validate' in validation_rule:
                for rule_name, rule_args in validation_rule['validate'].iteritems():
                    current_status = getattr(self._validator, rule_name)(*rule_args['param'])
                    self._inputs[current_input]['status'] = current_status
                    status &= current_status
                    if not current_status:
                        self._errors[current_input] = rule_args['error']

            # Set and return Overall status
            self._vstatus = status
            return status

    def sanitize(self):
        """Sanitize Inputs and Store Them"""
        for current_input, sanitization_rule in self._inputs.iteritems():
            # Push input value to sanitizer
            if self._type == 'form':
                self._inputs[current_input]['value'] = self._form.getfirst(current_input, '')
            self._sanitizer.set_input(self._inputs[current_input]['value'])

            # Sanitize current input value
            status = True
            if 'sanitize' in sanitization_rule:
                for rule_name, rule_args in sanitization_rule['sanitize'].iteritems():
                    sanitized_value = getattr(self._sanitizer, rule_name)(*rule_args['param'])
                    self._inputs[current_input]['svalue'] = sanitized_value
                    self._inputs[current_input]['is_exact'] = True if self._inputs[current_input]['value'] == sanitized_value else False
                    status &= self._inputs[current_input]['is_exact']

            # Set and return Overall status
            self._sstatus = status
            return status

