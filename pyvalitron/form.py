"""
Form
"""

from .validator import Validator
from .sanitizer import Sanitizer
from .exceptions import PyValitronError


class Form(object):

    _inputs = {}
    _errors = {}
    _sinputs = {}

    _vstatus = False
    _sstatus = False

    _validator = None
    _sanitizer = None
    _sanitizers = []
    _validators = []

    def __init__(self, inputs={}):
        """Init Form Module"""
        self._inputs = inputs
        self._validator = Validator()
        self._sanitizer = Sanitizer()

    def add_inputs(self, inputs={}):
        """Set inputs"""
        self._inputs = inputs

    def get_inputs(self):
        """Get Original Inputs Values"""
        return self._inputs

    def get_input(self, input_key):
        return self._inputs[input_key]["value"]

    def get_sinput(self, input_key):
        if "svalue" in self._inputs[input_key]:
            return self._inputs[input_key]["svalue"]
        else:
            return self.get_input(input_key)

    def get_errors(self):
        """Get All Errors"""
        return self._errors

    def is_passed(self):
        """Check if all inputs are valid"""
        for input in self._inputs:
            if len(self._errors[input]) > 0:
                return False
        return True

    def get_vstatus(self):
        """Get Overall Sanitization Status"""
        return self._vstatus

    def get_sstatus(self):
        """Get Overall Sanitization Status"""
        return self._sstatus

    def process(self, direction=['sanitize', 'validate']):
        """Process both validation and sanitization"""
        if direction[0] == 'sanitize':
            if 'sanitize' in direction:
                self._sanitize()
            if 'validate' in direction:
                self._validate()
        else:
            if 'validate' in direction:
                self._validate()
            if 'sanitize' in direction:
                self._sanitize()

    def add_validator(self, val_instance):
        """Add custom validator"""
        self._validators.append(val_instance)

    def add_sanitizer(self, san_instance):
        """Add custom sanitizer"""
        self._sanitizers.append(san_instance)

    def _validate(self):
        """Validate, Set Errors and Return Overall Status"""
        status = True
        for current_input, validation_rule in self._inputs.items():
            # Push input value to validator
            self._validator.set_input(self._inputs[current_input]['value'])
            if 'validate' in validation_rule:
                self._errors[current_input] = []
                for rule_name, rule_args in validation_rule['validate'].items():
                    self._update_validator(rule_name)
                    getattr(self._validator, "set_input")(self._inputs[current_input]['value'])
                    # Check if param exist and pass them to the method
                    if 'param' in rule_args.keys() and len(rule_args['param']) > 0:
                        current_status = getattr(self._validator, rule_name)(*rule_args['param'])
                    else:
                        current_status = getattr(self._validator, rule_name)()

                    if "optional" in validation_rule['validate'] and self._inputs[current_input]['value'] == "":
                        current_status = True

                    self._inputs[current_input]['status'] = current_status
                    status &= current_status
                    if not current_status and 'error' in rule_args.keys():
                        self._errors[current_input].append(rule_args['error'])

        # Set and return Overall status
        self._vstatus = status
        return status

    def _sanitize(self):
        """Sanitize Inputs and Store Them"""
        status = True
        for current_input, sanitization_rule in self._inputs.items():
            # Push input value to sanitizer
            self._sanitizer.set_input(self._inputs[current_input]['value'])
            self._sanitizer.set_sinput(None)
            if 'sanitize' in sanitization_rule:
                for rule_name, rule_args in sanitization_rule['sanitize'].items():
                    self._update_sanitizer(rule_name)
                    # Check if param provided and pass them to the method
                    if 'param' in rule_args.keys() and len(rule_args['param']) > 0:
                        sanitized_value = getattr(self._sanitizer, rule_name)(*rule_args['param'])
                    else:
                        sanitized_value = getattr(self._sanitizer, rule_name)()
                    self._inputs[current_input]['svalue'] = sanitized_value
                    self._inputs[current_input]['is_exact'] = True if self._inputs[current_input]['value'] == self._sanitizer.get_sinput() else False
                    status &= self._inputs[current_input]['is_exact']

        # Set and return Overall status
        self._sstatus = status
        return status

    def _update_validator(self, rule_name):
        """Update current validator"""
        if hasattr(self._validator, rule_name):
            return True
        for validator in self._validators:
            if hasattr(validator, rule_name):
                self._validator = validator
                return True
        raise PyValitronError('Non existent validation rule %s' % rule_name)

    def _update_sanitizer(self, rule_name):
        """Update current sanitizer"""
        if hasattr(self._sanitizer, rule_name):
            if self._sanitizer.get_sinput() is None:
                self._sanitizer.set_input(self._sanitizer.get_input())
                self._sanitizer.set_sinput(None)
            else:
                self._sanitizer.set_input(self._sanitizer.get_sinput())
            return True
        for sanitizer in self._sanitizers:
            if hasattr(sanitizer, rule_name):
                if self._sanitizer.get_sinput() is None:
                    sanitizer.set_input(self._sanitizer.get_input())
                    sanitizer.set_sinput(None)
                else:
                    sanitizer.set_input(self._sanitizer.get_sinput())
                self._sanitizer = sanitizer
                return True
        raise PyValitronError('Non existent sanitization rule %s' % rule_name)
