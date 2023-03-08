"""
Auto-replay chat robot abstract class
"""


class Bot(object):
    def ask(self, content):
        raise NotImplementedError

    def ask_stream(self, message):
        raise NotImplementedError
