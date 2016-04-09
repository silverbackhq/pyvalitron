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
        }, 'values').process()

if __name__ == '__main__':
    unittest.main()
