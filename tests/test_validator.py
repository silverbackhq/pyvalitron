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
    pass


    # validator = Validator();

    # validator.set_input(5)
    # print(validator.required())
    # print('-----------------------')
    # validator.set_input(5)
    # print(validator.greater_than(5))
    # print(validator.greater_than_equal(5))
    # print(validator.less_than(6))
    # print(validator.less_than_equal(4))
    # print(validator.equal(5))
    # print('-----------------------')
    # validator.set_input("Hello World")
    # print(validator.length_between(2, 12))
    # print(validator.min_length(1))
    # print(validator.max_length(11))
    # print(validator.exact_length(11))
    # print(validator.same_as('Hello World'))
    # print('-----------------------')
    # validator.set_input('1')
    # print(validator.any_of(['1']))
    # validator.set_input('6')
    # print(validator.none_of(['6']))
    # validator.set_input('5')
    # print(validator.none_of(['5']))
    # print('-----------------------')
    # validator.set_input('1')
    # print(validator.alpha())
    # print('-----------------------')
    # validator.set_input('sh')
    # print(validator.alpha_numeric())
    # print('-----------------------')
    # validator.set_input('0.0.0.0')
    # print(validator.ip())
    # validator.set_input('192.0168.1.1')
    # print(validator.ip())
    # validator.set_input('255.255.255.255')
    # print(validator.ip())
    # validator.set_input('0000:0000:0000:0000:0000:0000:0000:0000')
    # print(validator.ip())
    # validator.set_input('fe00::1')
    # print(validator.ip())
    # validator.set_input('fe80::217:f2ff:fe07:ed62')
    # print(validator.ip())
    # validator.set_input('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
    # print(validator.ip())
    # validator.set_input('2001:0db8:0000:85a3:0000:0000:ac1f:8001')
    # print(validator.ip())

    # print('-----------------------')
    # validator.set_input('dd@ddd.comss')
    # print(validator.email())
    # validator.set_input('hello@clivern.com,szdv@dc.cccc.c')
    # print(validator.emails())


    # validator.set_input('ftp://clivern.biz')
    # print(validator.url())