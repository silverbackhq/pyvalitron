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
import unittest


class TestValidatorMethods(unittest.TestCase):

    def test_validator(self):
        validator = Validator()

        validator.set_input('')
        self.assertEqual(True, validator.empty())

        validator.set_input('Hello World')
        self.assertEqual(True, validator.not_empty())

        validator.set_input("Hello World")
        self.assertEqual(True, validator.length_between(1, 12))
        self.assertEqual(True, validator.min_length(1))
        self.assertEqual(True, validator.max_length(11))
        self.assertEqual(True, validator.exact_length(11))

        validator.set_input(5)
        self.assertEqual(True, validator.greater_than(4))
        self.assertEqual(True, validator.greater_than_equal(5))
        self.assertEqual(True, validator.less_than(6))
        self.assertEqual(True, validator.less_than_equal(5))
        self.assertEqual(True, validator.equal(5))

        validator.set_input("Hello World")
        self.assertEqual(True, validator.same_as("Hello World"))

        validator.set_input(9)
        self.assertEqual(True, validator.any_of([9, 5, 6, 20]))
        self.assertEqual(True, validator.none_of([8, 7, 5, 6]))

        validator.set_input([1, 4, 8, 9])
        self.assertEqual(True, validator.all_of([1, 4, 8, 9]))

        validator.set_input('hello')
        self.assertEqual(True, validator.alpha())

        validator.set_input('hello2')
        self.assertEqual(True, validator.alpha_numeric())

        validator.set_input('888888')
        self.assertEqual(True, validator.digit())

        validator.set_input('hello@clivern.com')
        self.assertEqual(True, validator.email())

        validator.set_input('hello@clivern.com,support@clivern.com')
        self.assertEqual(True, validator.emails())

        validator.set_input('http://clivern.com')
        self.assertEqual(True, validator.url())

        validator.set_input('192.168.0.1')
        self.assertEqual(True, validator.ip())

        validator.set_input('192.168.0.1')
        self.assertEqual(True, validator.ipv4())

        validator.set_input('hello@clivern.com')
        self.assertEqual(True, validator.matches(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,5})$'))

if __name__ == '__main__':
    unittest.main()
