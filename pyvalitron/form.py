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
    _sanitizers = []
    _validators = []
    _utils = None

    def __init__(self, inputs = {}, inputs_type='form'):
        """Init Form Module"""
        self._type = inputs_type
        self._inputs = inputs
        self._validator = Validator()
        self._sanitizer = Sanitizer()
        self._utils = Utils()

    def add_inputs(self, inputs = {}):
        """Set inputs"""
        self._inputs = inputs

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

    def process(self):
        if self._type == 'form':
            self._form = cgi.FieldStorage()
        self._validate()
        self._sanitize()

    def add_validator(self, val_instance):
        """Add custom validator"""
        self._validators.append(val_instance)

    def add_sanitizer(self, san_instance):
        """Add custom sanitizer"""
        self._sanitizers.append(san_instance)

    def _validate(self):
        """Validate, Set Errors and Return Overall Status"""

        # Validate current inputs value
        status = True

        for current_input, validation_rule in self._inputs.items():
            # Push input value to validator
            if self._type == 'form':
                self._inputs[current_input]['value'] = self._form.getfirst(current_input, '')
            self._validator.set_input(self._inputs[current_input]['value'])
            if 'validate' in validation_rule:
                self._errors[current_input] = []
                for rule_name, rule_args in validation_rule['validate'].items():
                    self._update_validator(rule_name)
                    # Check if param exist and pass them to the method
                    if 'param' in rule_args.keys() and len(rule_args['param']) > 0:
                        current_status = getattr(self._validator, rule_name)(*rule_args['param'])
                    else:
                        current_status = getattr(self._validator, rule_name)()
                    self._inputs[current_input]['status'] = current_status
                    status &= current_status
                    if not current_status and 'error' in rule_args.keys():
                        self._errors[current_input].append(rule_args['error'])

        # Set and return Overall status
        self._vstatus = status
        return status

    def _sanitize(self):
        """Sanitize Inputs and Store Them"""

        # Sanitize current input value
        status = True

        for current_input, sanitization_rule in self._inputs.items():
            # Push input value to sanitizer
            if self._type == 'form':
                self._inputs[current_input]['value'] = self._form.getfirst(current_input, '')
            self._sanitizer.set_input(self._inputs[current_input]['value'])
            if 'sanitize' in sanitization_rule:
                for rule_name, rule_args in sanitization_rule['sanitize'].items():
                    self._update_sanitizer(rule_name)
                    # Check if param provided and pass them to the method
                    if 'param' in rule_args.keys() and len(rule_args['param']) > 0:
                        sanitized_value = getattr(self._sanitizer, rule_name)(*rule_args['param'])
                    else:
                        sanitized_value = getattr(self._sanitizer, rule_name)()
                    self._inputs[current_input]['svalue'] = sanitized_value
                    self._inputs[current_input]['is_exact'] = True if self._sanitizer.get_input() == self._sanitizer.get_sinput() else False
                    status &= self._inputs[current_input]['is_exact']

        # Set and return Overall status
        self._sstatus = status
        return status

    def _update_validator(self, rule_name):
        """Update current validator"""
        if hasattr(self._validator, rule_name):
            return True
        for validator in self._validators:
            if hasattr(validator, rule_name):
                self._validator = validator
                return True
        raise PyValitronError('Non existent validation rule %s' % rule_name)

    def _update_sanitizer(self, rule_name):
        """Update current sanitizer"""
        if hasattr(self._sanitizer, rule_name):
            return True
        for sanitizer in self._sanitizers:
            if hasattr(sanitizer, rule_name):
                sanitizer.set_input(self._sanitizer.get_input())
                sanitizer.set_sinput(self._sanitizer.get_sinput())
                self._sanitizer = sanitizer
                return True
        raise PyValitronError('Non existent sanitization rule %s' % rule_name)
