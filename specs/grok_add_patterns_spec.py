from pspec import describe
from grok import Grok


with describe('grok.Grok'):
    def it_adds_a_single_pattern():
        grok = Grok()
        grok.add_pattern('name', '%{PATTERN}')

        assert 'name' in grok.patterns
        assert '%{PATTERN}' == grok.patterns['name']
        assert 1 == len(grok.patterns.keys())
