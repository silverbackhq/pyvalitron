# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

class Sanitizer(object):

    _input = None
    _sinput = None

    def set_input(self, input_value):
        self._input = input_value

    def get_sinput(self):
        return self._sinput

    def get_input(self):
        return self._input

    def is_exact(self):
        return self._input == self._sinput and len(self._input) == len(self._sinput)

    def trim(self):
        pass

    def escape(self):
        pass
