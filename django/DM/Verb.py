__author__ = 'zice'


class Verb:
    name = ''
    prior = dict()
    next = dict()

    def __int__(self, name):
        self.name = name

