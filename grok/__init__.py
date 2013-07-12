import re
import copy
import logging
from .exceptions import PatternException, PatternMaxRecursionException

logger = logging.getLogger('grok.Grok')

PATTERN_RE = re.compile('%{(?P<pattern>[a-zA-Z0-9]+)}')


class Grok(object):

    expanded_pattern = None

    def __init__(self):
        self.patterns = {}

    def add_pattern(self, name, pattern):
        logger.info('Adding pattern %{name}: %{pattern}'.format(name=name, pattern=pattern))
        self.patterns[name] = pattern

    def add_patterns_from_file(self, file):
        with open(file, 'r') as fh:
            for line in fh.readlines():
                if re.compile(r'^[a-zA-Z0-9_]+\s.*$').match(line):
                    name, pattern = re.compile(r'\s+').split(line.lstrip(), 1)
                    self.add_pattern(name.strip(), pattern.strip())

    def compile(self, pattern):
        self.pattern = pattern
        self.expanded_pattern = copy.copy(pattern)

        iterations_left = 100
        while iterations_left > 0:
            logger.info('Iteration {it}'.format(it=iterations_left))
            iterations_left -= 1
            m = PATTERN_RE.search(self.expanded_pattern)
            if not m:
                break
            mp = m.groupdict()['pattern']
            if mp in self.patterns:
                regex = self.patterns[mp]
                logger.debug('should replace %s with %s' % (mp, self.patterns[mp]))
                self.expanded_pattern = self.expanded_pattern.replace('%{'+mp+'}', self.patterns[mp])
            else:
                raise PatternException('Pattern {pattern} not defined!'.format(pattern=mp))
        else:
            raise PatternMaxRecursionException("Deep recursion pattern compilation of {pattern} - {expanded}".format(pattern=pattern, expanded=self.expanded_pattern))

        self.regexp = re.compile(self.expanded_pattern)
        logger.debug('Grok compiled OK pattern: {pattern}, expanded_pattern: {expanded}'.format(
            pattern=pattern, expanded=self.expanded_pattern))

    def discover(self, input):
        pass
