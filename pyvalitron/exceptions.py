"""
Custome Exceptions
"""


class PyValitronError(Exception):
    """Validation Custom Exceptions module"""

    def __init__(self, error_info):
        Exception.__init__(self, "PyValitron exception was raised")
        self.error_info = error_info
