import logging

logger = logging.getLogger('grok.Grok')


class Grok(object):

    extended_pattern = None

    def __init__(self):
        self.patterns = {}

    def add_pattern(self, name, pattern):
        logger.warn('Adding pattern %{name}: %{pattern}'.format(name=name, pattern=pattern))
        self.patterns[name] = pattern

    def add_patterns_from_file(self, file):
        pass

    def compile(self, pattern):
        pass

    def discover(self, input):
        pass
