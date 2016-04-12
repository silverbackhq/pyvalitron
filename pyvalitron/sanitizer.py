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

    def strip(self, chars = ''):
        """Strip input value"""
        if not isinstance(self._input, (str)):
            self._input = str(self._input)

        if len(chars) > 0:
            self._input = self._input.strip(chars)
        else:
            self._input = self._input.strip()

        return self._input

    def lstrip(self, chars = ''):
        """Left strip input value"""
        if not isinstance(self._input, (str)):
            self._input = str(self._input)

        if len(chars) > 0:
            self._input = self._input.lstrip(chars)
        else:
            self._input = self._input.lstrip()

        return self._input

    def rstrip(self, chars = ''):
        """Right strip input value"""
        if not isinstance(self._input, (str)):
            self._input = str(self._input)

        if len(chars) > 0:
            self._input = self._input.rstrip(chars)
        else:
            self._input = self._input.rstrip()

        return self._input

    def escape(self, chars=['&', '"', '\'', '>', '<']):
        """Escape input value"""
        html_escape_table = {
            "&": "&amp;" if '&' in chars else '&',
            '"': "&quot;" if '"' in chars else '"',
            "'": "&apos;" if '\'' in chars else '\'',
            ">": "&gt;" if '>' in chars else '>',
            "<": "&lt;" if '<' in chars else '<',
        }

        if not isinstance(self._input, (str)):
            self._input = str(self._input)

        self._input = "".join(html_escape_table.get(c,c) for c in self._input)
        return self._input
