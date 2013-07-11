import unittest
from grok import Grok

@unittest.skip("Not yet implemented")
class GrokAddPatternTest(unittest.TestCase):

    def setUp(self):
        self.grok = Grok()

    def test_parses_ISO8601_successfully(self):
        self.grok.add_patterns_from_file('patterns/base')

        date = '2010-04-18T15:06:02Z'
        pattern = '%{TIMESTAMP_ISO8601}'

        self.compile(pattern)

        self.assertTrue("%{YEAR}-%{MONTHNUM}-%{MONTHDAY}[T ]%{HOUR}:?%{MINUTE}(?::?%{SECOND})?%{ISO8601_TIMEZONE}?" == self.grok.extended_pattern)
        self.assertTrue(selg.grok.match(date))

    def test_parses_ISO8601_successfully(self):
        self.grok.add_patterns_from_file('patterns/base')

        string = "http://www.google.com/ and 00:de:ad:be:ef:00 with 'Something Nice'"
        pattern = self.grok.discover(string)

        self.assertTrue("%{MAC}" == pattern)
