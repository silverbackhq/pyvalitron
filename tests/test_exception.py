from __future__ import print_function
from pyvalitron.exceptions import PyValitronError
import unittest


class TestExceptionMethods(unittest.TestCase):

    def test_error(self):
        try:
            raise PyValitronError('Error raised with %s' % 'dynamic data')
        except Exception as e:
            self.assertEqual(e.error_info, 'Error raised with dynamic data')


if __name__ == '__main__':
    unittest.main()
