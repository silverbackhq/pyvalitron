# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""
import re


class Validator(object):

    _input = None
    _errors = {}
    _required = False

    def set_input(self, input_value):
        self._input = input_value

    def required(self):
        """Validate if input has no empty value"""
        return not self._input == ''

    def length_between(self, from_length, to_length):
        """Validate if input length is between provided length limits"""
        if to_length > len(self._input) > from_length:
            return True
        else:
            return False

    def min_length(self, min_length):
        """Validate if input length is greater that provided length"""
        if len(self._input) >= min_length:
            return True
        else:
            return False

    def max_length(self, max_length):
        """Validate if input length is less that provided length"""
        if len(self._input) <= max_length:
            return True
        else:
            return False

    def exact_length(self, exact_length):
        """Validate if input length is equal to provided one"""
        if len(self._input) == exact_length:
            return True
        else:
            return False

    def greater_than(self, number):
        """Validate if input is greater than provided one"""
        if self._input > number:
            return True
        else:
            return False

    def greater_than_equal(self, number):
        """Validate if input is greater than or equal provided one"""
        if self._input >= number:
            return True
        else:
            return False

    def less_than(self, number):
        """Validate if input is less than provided one"""
        if self._input < number:
            return True
        else:
            return False

    def less_than_equal(self, number):
        """Validate if input is less than or equal provided one"""
        if self._input <= number:
            return True
        else:
            return False

    def equal(self, number):
        """Validate if input is equal to provided one"""
        if self._input == number:
            return True
        else:
            return False

    def same_as(self, text):
        """Validate if input is the same as provided one"""
        if self._input == text:
            return True
        else:
            return False

    def enum(self, options):
        """Validate if input in a list"""
        return self._input in options

    def alpha(self):
        """Validate if input is alph"""
        if not isinstance(self._input, (str)):
            return False
        return self._input.isalpha()

    def alpha_numeric(self):
        """Validate if input is alpha numeric"""
        if not isinstance(self._input, (str)):
            return False
        return self._input.isalnum()

    def digit(self):
        """Validate if input is digits"""
        if not isinstance(self._input, (str)):
            return False
        return self._input.isdigit()

    #def integer(self):
    #    if not isinstance(self._input, (float)):
    #        return False
    #    return self._input.is_integer()

    #def numeric(self):
    #    if not isinstance(self._input, (unicode)):
    #        return False
    #    return self._input.isnumeric()

    #def decimal(self):
    #    if not isinstance(self._input, (unicode)):
    #        return False
    #    return self._input.isdecimal()


    def email(self):
        """Validate if input is a valid email address"""
        return bool(re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,5})$', self._input ,re.IGNORECASE))

    def emails(self, sep=','):
        """Validate if input is a valid list of email addresses"""
        status = True
        for email in self._input.split(sep):
            status &= bool(re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,5})$', email ,re.IGNORECASE))
        return status

    def url(self, protocols=['http', 'https'], relative = False):
        """Validate if input is a valid URL"""
        pass

    def ip(self, formats=['ipv4']):
        """Validates an IP address."""
        if 'ipv4' in formats:
            return self.ipv4()
        else:
            return False

    def ipv4(self):
        """Validates an IPv4 address."""
        parts = self._input.split('.')
        if len(parts) == 4 and all(x.isdigit() for x in parts):
            numbers = list(int(x) for x in parts)
            return all(num >= 0 and num < 256 for num in numbers)
        return False

    def matches(self, regex, flags=0):
        """Validate if input match the provided regexp"""
        if isinstance(regex, string_types):
            regex = re.compile(regex, flags)

        if regex.match(self._input):
            return True
        else:
            return False

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

if __name__ == '__main__':
    validator = Validator();

    validator.set_input(5)
    print(validator.required())
    print('-----------------------')
    validator.set_input(5)
    print(validator.greater_than(5))
    print(validator.greater_than_equal(5))
    print(validator.less_than(6))
    print(validator.less_than_equal(4))
    print(validator.equal(5))
    print('-----------------------')
    validator.set_input("Hello World")
    print(validator.length_between(2, 12))
    print(validator.min_length(1))
    print(validator.max_length(11))
    print(validator.exact_length(11))
    print(validator.same_as('Hello World'))
    print('-----------------------')
    validator.set_input('1')
    print(validator.enum(['1']))
    print('-----------------------')
    validator.set_input('1')
    print(validator.alpha())
    print('-----------------------')
    validator.set_input('sh')
    print(validator.alpha_numeric())
    print('-----------------------')
    validator.set_input('0.0.0.0')
    print(validator.ip())
    validator.set_input('192.0168.1.1')
    print(validator.ip())
    validator.set_input('255.255.255.255')
    print(validator.ip())
    validator.set_input('0000:0000:0000:0000:0000:0000:0000:0000')
    print(validator.ip())
    validator.set_input('fe00::1')
    print(validator.ip())
    validator.set_input('fe80::217:f2ff:fe07:ed62')
    print(validator.ip())
    validator.set_input('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
    print(validator.ip())
    validator.set_input('2001:0db8:0000:85a3:0000:0000:ac1f:8001')
    print(validator.ip())


    print('-----------------------')
    validator.set_input('dd@ddd.comss')
    print(validator.email())
    validator.set_input('hello@clivern.com,szdv@dc.cccc.c')
    print(validator.emails())