PyValitron
==========

PyValitron is a light-weight python inputs validation library.

*Current version: [v1.0.0-dev]*

[![Build Status](https://travis-ci.org/Clivern/PyValitron.svg?branch=master)](https://travis-ci.org/Clivern/PyValitron)

Installation
------------
To install PyLogging run this command:
```
pip install pyvalitron
```
or [download](https://github.com/Clivern/pyvalitron/archive/1.0.0.zip) Package then run this command:
```
pip install PyValitron-1.0.0.zip
```

Usage
-----
After installing the library, Read the following usage criteria:

### Using Validator
The typical usage of form validator is like the following:
```

```

#### Validators List:

* `empty`: Validate if input or a value is empty.
* `not_empty`: Validate if input or a value is not empty.
* `length_between`: Validate if input or a value length is between provided lengths. It requires two parameters `[from_length, to_length]` like `[1, 13]`.
* `min_length`: Validate if input or a value min lenght is like provided one. It requires one parameter `[min_length]` like `[1]`.
* `max_length`: Validate if input or a value max lenght is like provided one. It requires one parameter `[max_length]` like `[12]`.
* `exact_length`: Validate if input or a value lenght is equal to provided one. It requires one parameter `[exact_length]` like `[9]`.
* `greater_than`: Validate if input or a value is greater than provided one. It requires one parameter `[number]` like `[5]`.
* `greater_than_equal`: Validate if input or a value is greater than or equal provided one. It requires one parameter `[number]` like `[4]`.
* `less_than`: Validate if input or a value is less than provided one. It requires one parameter `[number]` like `[5]`.
* `less_than_equal`: Validate if input or a value is less than or equal provided one. It requires one parameter `[number]` like `[5]`.
* `equal`: Validate if input or a value is equal to provided one. It requires one parameter `[number]` like `[5]`.
* `same_as`: Validate if input or a value is same as provided one. It requires one parameter `[text]` like `['Hello World']`
* `any_of`: Validate if input or a value is any of the provided list. It requires one parameter `[[options]]` like `[1,5,'text']`.
* `all_of`: Validate if input or a value is all of the provided list. It requires one parameter `[[options]]` like `[1,5,'text']`.
* `none_of`: Validate if input or a value is none of the provided list. It requires one parameter `[[options]]` like `[1,5,'text']`.
* `alpha`: Validate if input or a value is alphabetical.
* `alpha_numeric`: Validate if input or a value is alphanumeric.
* `digit`: Validate if input or a value is digits.
* `email`: Validate if input or a value is email.
* `emails`: Validate if input or a value is a list of emails. It requires one parameter `[separator]` like `[',']`.
* `url`: Validate if input or a value is a URL. It requires one parameter (a list of protocols) `[[protocols]]` like `[['http', 'https']]`.
* `ip`: Validate if input or a value is IP. It requires one parameter (a list of formats) `[[formats]]` like `['ipv4']`
* `ipv4`: Validate if input or a value is IPv4.
* `uuid`: Validate if input or a value is universally unique identifier (UUID)
* `matches`: Validate if input or a value matches provided regex. It requires one parameter `[regex]` like `[r'^[_a-z0-9-]+$']`.


### Using Sanitizer
The typical usage of form sanitizer is like the following:
```

```

#### Sanitizers List

*
*
*

### Custom Validators

To define a new validator:
```
class MyValidator(Validator):

    def username(self):
        if not isinstance(self._input, (str)):
            return False
        current_input = self._input.strip()
        if len(current_input) > 5 and current_input.isalpha():
            return True
        return False

    def otherrule(self):
        return True

    #...and so one

form = Form()
form.add_validator(MyValidator())
form.add_inputs({
    'user_name': {
        'value': '',
        'validate': {
            'username': {
                'error': 'Invalid Username'
            }
        }
    }
})
form.process()
errors = form.get_errors()
```

### Custom Sanitizers

To define a new sanitizer:
```

```

Misc
====

Changelog
---------

Version 1.0.0 (coming soon):
```
Initial Release.
```

Acknowledgements
----------------

© 2016, Clivern. Released under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

**PyLogging** is authored and maintained by [@clivern](http://github.com/clivern).