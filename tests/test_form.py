from __future__ import print_function
from pyvalitron.validator import Validator
from pyvalitron.sanitizer import Sanitizer
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


class MySanitizer(Sanitizer):

    def clear_spaces(self):
        if not isinstance(self._input, (str)):
            self._sinput = str(self._input)
        else:
            self._sinput = self._input

        self._sinput = self._sinput.replace(" ", "")
        return self._sinput

    def lower_case(self):
        if not isinstance(self._input, (str)):
            self._sinput = str(self._input)
        else:
            self._sinput = self._input
        self._sinput = self._sinput.lower()
        return self._sinput


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
        })
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
                    'length_between': {
                        'param': [1, 12],
                        'error': 'Input lenght must be between 1 and 12 characters'
                    }
                }
            },
            'test_field2': {
                'value': 'Hello World',
                'validate': {
                    'length_between': {
                        'param': [1, 9],
                        'error': 'Input lenght must be between 1 and 9 characters'
                    }
                }
            }
        })
        form.process()
        errors = form.get_errors()
        self.assertEqual(0, len(errors['test_field1']))
        self.assertEqual(1, len(errors['test_field2']))
        self.assertEqual(True, 'Input lenght must be between 1 and 9 characters' in errors['test_field2'])

    def test_custom_validator(self):
        form = Form({
            'user_name': {
                'value': '',
                'validate': {
                    'username': {
                        'error': 'Invalid Username'
                    }
                }
            }
        })
        form.add_validator(MyValidator())
        form.process()
        errors = form.get_errors()
        self.assertEqual(1, len(errors['user_name']))
        self.assertEqual(True, 'Invalid Username' in errors['user_name'])

    def test_custom_sanitizer(self):
        form = Form({
            'test_field': {
                'value': 'Hello World',
                'sanitize': {
                    'clear_spaces': {},
                    'lower_case': {}
                }
            }
        })
        form.add_sanitizer(MySanitizer())
        form.process()
        inputs = form.get_inputs()
        self.assertEqual('helloworld', inputs['test_field']['svalue'])

    def test_validation_sanitization(self):
        form = Form({
            'test_field': {
                'value': 'hello@clivern.com',
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            }
        })
        form.process()
        inputs = form.get_inputs()
        errors = form.get_errors()
        self.assertEqual([], errors['test_field'])
        self.assertEqual(True, inputs['test_field']['status'])
        self.assertEqual(True, inputs['test_field']['is_exact'])
        self.assertEqual('hello@clivern.com', inputs['test_field']['value'])
        self.assertEqual('hello@clivern.com', inputs['test_field']['svalue'])

        form = Form({
            'test_field': {
                'value': 'hello@cliv@ern.com',
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            }
        })
        form.process()
        inputs = form.get_inputs()
        errors = form.get_errors()
        self.assertEqual(['Please provide a valid email.'], errors['test_field'])
        self.assertEqual(False, inputs['test_field']['status'])
        self.assertEqual(True, inputs['test_field']['is_exact'])
        self.assertEqual('hello@cliv@ern.com', inputs['test_field']['value'])
        self.assertEqual('hello@cliv@ern.com', inputs['test_field']['svalue'])


if __name__ == '__main__':
    unittest.main()
