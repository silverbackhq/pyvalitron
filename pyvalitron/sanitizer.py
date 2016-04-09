# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""


class Sanitizer(object):
    """Sanitize Inputs Module"""

    # Input Value
    _input = None

    # Sanitized Input Value
    _sinput = None

    def set_input(self, input_value):
        """Set Input Value"""
        self._input = input_value

    def get_sinput(self):
        """Get sanitized input value"""
        return self._sinput

    def get_input(self):
        """Get original input value"""
        return self._input

    def is_exact(self):
        """Check if original and sanitized value are the same"""
        return self._input == self._sinput and len(self._input) == len(self._sinput)

    def trim(self):
        """Trim input value"""
        pass

    def escape(self):
        """Escape input value"""
        pass
