# -*- coding: utf-8 -*-


class Request(object):
    def __init__(self):
        self.method = ''
        self.uri = ''
        self.headers = {}
        self.body = ''

    def __str__(self):
        return '{} {}'.format(self.method, self.uri)
    