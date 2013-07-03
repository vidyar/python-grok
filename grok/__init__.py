import re
import logging

logger = logging.getLogger('grok.Grok')


class Grok(object):

    extended_pattern = None

    def __init__(self):
        self.patterns = {}

    def add_pattern(self, name, pattern):
        logger.info('Adding pattern %{name}: %{pattern}'.format(name=name, pattern=pattern))
        self.patterns[name] = pattern

    def add_patterns_from_file(self, file):
        with open(file, 'r') as fh:
            for line in fh.readlines():
                if re.compile(r'^(\s*#\s*|\s*$)').match(line):
                    continue
                name, pattern = re.compile(r'\s+').split(line.lstrip(), 1)
                self.add_pattern(name, pattern.strip())

    def compile(self, pattern):
        pass

    def discover(self, input):
        pass
