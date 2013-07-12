import unittest
from grok import Grok
from grok.exceptions import PatternException, PatternMaxRecursionException


class TestGrokCompile(unittest.TestCase):

    def setUp(self):
        self.grok = Grok()

    def test_compile_no_matches(self):
        self.grok.add_pattern('PATTERN', '[a-zA-Z]')
        pattern = 'no pattern to see, move along'
        self.grok.compile(pattern)
        self.assertEquals(pattern, self.grok.expanded_pattern)

    def test_compile_pattern_not_found(self):
        self.grok.add_pattern('PATTERN', '[a-zA-Z]')
        pattern = '%{OTHERPATTERN}'

        with self.assertRaises(PatternException):
            self.grok.compile(pattern)

    def test_compile_single_match(self):
        self.grok.add_pattern('PATTERN', '[a-zA-Z]')
        pattern = '[a-z]%{PATTERN}'
        self.grok.compile(pattern)
        self.assertEquals('[a-z][a-zA-Z]', self.grok.expanded_pattern)

    def test_compile_max_recursion(self):
        self.grok.add_pattern('PATTERN', '%{PATTERN}')
        pattern = '%{PATTERN}'
        with self.assertRaises(PatternMaxRecursionException):
            self.grok.compile(pattern)

