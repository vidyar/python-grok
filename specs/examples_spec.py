from pspec import describe
from grok import Grok


with describe('grok.Grok'):
    def it_parses_ISO8601():
        grok = Grok()
        grok.add_patterns_from_file('../patterns/base')

        input = '2010-04-18T15:06:02Z'
        pattern = '%{TIMESTAMP_ISO8601}'

        grok.compile(pattern)

        assert "%{YEAR}-%{MONTHNUM}-%{MONTHDAY}[T ]%{HOUR}:?%{MINUTE}(?::?%{SECOND})?%{ISO8601_TIMEZONE}?" == grok.extended_pattern
        assert grok.match(input)

    def it_discovers_MAC():
        grok = Grok()
        grok.add_patterns_from_file('../patterns/base')

        input = "http://www.google.com/ and 00:de:ad:be:ef:00 with 'Something Nice'"
        pattern = grok.discover(input)

        assert "%{MAC}" == pattern
