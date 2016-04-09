# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""
from __future__ import print_function
from pyvalitron.form import Form
import unittest


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
        self.assertEqual('User email must be provided', errors['user_email'][0])
        self.assertEqual('User email is invalid', errors['user_email'][1])

if __name__ == '__main__':
    unittest.main()
