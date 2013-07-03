from pspec import describe
from grok import Grok


with describe('grok.Grok'):
    def it_adds_a_single_pattern():
        grok = Grok()
        grok.add_pattern('name', '%{PATTERN}')

        assert 'name' in grok.patterns
        assert '%{PATTERN}' == grok.patterns['name']
        assert 1 == len(grok.patterns.keys())

    def it_adds_patterns_from_file():
        grok = Grok()
        grok.add_patterns_from_file('specs/test-patterns/base')

        assert 2 == len(grok.patterns.keys())
        assert 'INT' in grok.patterns
        assert '(?:[+-]?(?:[0-9]+))' == grok.patterns['INT']
        assert 'BASE10NUM' in grok.patterns
        assert '(?<![0-9.+-])(?>[+-]?(?:(?:[0-9]+(?:\.[0-9]+)?)|(?:\.[0-9]+)))' == grok.patterns['BASE10NUM']
