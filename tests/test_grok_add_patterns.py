from unittest import TestCase
from grok import Grok


class GrokAddPatternTest(TestCase):

    def setUp(self):
        self.grok = Grok()

    def test_adds_a_single_pattern(self):
        self.grok.add_pattern('name', '%{PATTERN}')

        self.assertTrue('name' in self.grok.patterns)
        self.assertEquals('%{PATTERN}', self.grok.patterns['name'])
        self.assertEquals(1, len(self.grok.patterns.keys()))

    def test_adds_patterns_from_file(self):
        self.grok.add_patterns_from_file('tests/test-patterns/base')

        self.assertEquals(2, len(self.grok.patterns.keys()))
        self.assertTrue('INT' in self.grok.patterns)
        self.assertTrue('(?:[+-]?(?:[0-9]+))' == self.grok.patterns['INT'])
        self.assertTrue('BASE10NUM' in self.grok.patterns)
        self.assertTrue('(?<![0-9.+-])(?>[+-]?(?:(?:[0-9]+(?:\.[0-9]+)?)|(?:\.[0-9]+)))' == self.grok.patterns['BASE10NUM'])
