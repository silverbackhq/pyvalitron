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
                        'error': 'User email must be provided'
                    },
                    'email': {
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

    def test_form_validation_with_param(self):
        form = Form({
            'test_field1': {
                'value': 'Hello World',
                'validate': {
                    'length_between':{
                        'param': [1, 12],
                        'error': 'Input lenght must be between 1 and 12 characters'
                    }
                }
            },
            'test_field2': {
                'value': 'Hello World',
                'validate': {
                    'length_between':{
                        'param': [1, 9],
                        'error': 'Input lenght must be between 1 and 12 characters'
                    }
                }
            }
        }, 'values')
        form.process()
        errors = form.get_errors()
        self.assertEqual(0, len(errors['test_field1']))
        self.assertEqual(1, len(errors['test_field2']))
        self.assertEqual(True, 'Input lenght must be between 1 and 12 characters' in errors['test_field2'])

    def test_custom_validator(self):
        form = Form({
            'user_name': {
                'value': '',
                'validate': {
                    'username':{
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
