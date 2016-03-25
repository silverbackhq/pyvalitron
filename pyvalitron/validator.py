# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""


class Validator(object):

    _input = None
    _errors = {}
    _required = False

    def set_input(self, input_value):
        self._input = input_value

    def required(self):
        pass

    def lenght_between(self, from, to):
        pass

    def min_length(self, lenght):
        pass

    def max_length(self, length):
        pass

    def exact_length(self, length):
        pass

    def greater_than(self, number):
        pass

    def less_than(self, number):
        pass

    def email(self):
        pass

    def emails(self, sep=','):
        pass

    def ip(self, formats=['ip4']):
        pass

    def alnum(self, options):
        pass

    def integer(self):
        pass

    def numeric(self):
        pass

    def decimal(self):
        pass

    def matches(self, regexp):
        pass

    def alpha(self):
        pass

    def alpha_numeric(self):
        pass

    def alpha_dash(self):
        pass

    def base64(self):
        pass

    def get_errors(self):
        """Get a list of errors"""
        return self._errors

    def errors_exist(self):
        """Check if errors exist"""
        return True if len(self._errors) > 0 else False

    def clear_errors(self):
        """Clear all catched errors"""
        self._errors = {}

    def _set_error(self, vrule, error):
        """Set catched error"""
        if vrule == '' or error == '':
            return False
        else:
            self._errors[vrule] = error
        return True