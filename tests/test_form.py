# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""
from __future__ import print_function
from pyvalitron.validator import Validator
from pyvalitron.form import Form
import unittest


class MyValidator(Validator):

    def username(self):
        if not isinstance(self._input, (str)):
            return False
        current_input = self._input.strip()
        if len(current_input) > 5 and current_input.isalpha():
            return True
        return False


class TestFormMethods(unittest.TestCase):

    def test_form(self):
        form = Form({
            'user_email': {
                'value': '',
                'validate': {
                    'not_empty': {
                        'param': [],
                        'error': 'User email must be provided'
                    },
                    'email': {
                        'param': [],
                        'error': 'User email is invalid'
                    }
                }
            }
        }, 'values')
        form.process()
        errors = form.get_errors()
        self.assertEqual(2, len(errors['user_email']))
        self.assertEqual(True, 'User email must be provided' in errors['user_email'])
        self.assertEqual(True, 'User email is invalid' in errors['user_email'])

    def test_custom_validator(self):
        form = Form({
            'user_email': {
                'value': '',
                'validate': {
                    'not_empty': {
                        'param': [],
                        'error': 'User email must be provided'
                    },
                    'email': {
                        'param': [],
                        'error': 'User email is invalid'
                    }
                }
            },
            'user_name': {
                'value': '',
                'validate': {
                    'username':{
                        'param': [],
                        'error': 'Invalid Username'
                    }
                }
            }
        }, 'values')
        form.add_validator(MyValidator())
        form.process()
        errors = form.get_errors()
        self.assertEqual(1, len(errors['user_name']))
        self.assertEqual(True, 'Invalid Username' in errors['user_name'])

if __name__ == '__main__':
    unittest.main()
