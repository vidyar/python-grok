import unittest
from grok import PATTERN_RE


class TestGrokPatternRe(unittest.TestCase):

    def test_simple_pattern_capture(self):
        tests = '%{NAME},%{INT10},0%{NAME},%{NAME}0,0%{NAME}0,%{NAME}0,0%{NAME}'.split(',')
        for t in tests:
            m = PATTERN_RE.search(t)
            self.assertTrue(m and True)
            self.assertTrue('pattern' in m.groupdict())
            print t
