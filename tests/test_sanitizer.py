from __future__ import print_function
from pyvalitron.sanitizer import Sanitizer
import unittest


class TestSanitizerMethods(unittest.TestCase):

    def test_sanitizer(self):
        sanitizer = Sanitizer()

        text = '  Hello World.  '
        sanitizer.set_input(text)
        self.assertEqual(16, len(text))

        text = '  Hello World.  '
        sanitizer.set_input(text)
        self.assertEqual('Hello World.', sanitizer.strip())

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual(12, len(sanitizer.strip()))

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual('Hello World', sanitizer.strip('.'))

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual(11, len(sanitizer.strip('.')))

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual('Hello World', sanitizer.rstrip('.'))

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual(11, len(sanitizer.rstrip('.')))

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual('Hello World.', sanitizer.lstrip('.'))

        text = 'Hello World.'
        sanitizer.set_input(text)
        self.assertEqual(12, len(sanitizer.lstrip('.')))

        text = 'Hello& W"or"l\'d<br>.'
        sanitizer.set_input(text)
        self.assertEqual("Hello&amp; W&quot;or&quot;l&apos;d&lt;br&gt;.", sanitizer.escape())

        text = 'Hello& W"or"l\'d<br>.'
        sanitizer.set_input(text)
        self.assertEqual(45, len(sanitizer.escape()))


if __name__ == '__main__':
    unittest.main()
