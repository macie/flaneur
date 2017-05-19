# -*- coding: utf-8 -*-


class Response(object):
    def __init__(self, content=''):
        self.status = 200
        self.reason = 'OK'
        self.headers = {}
        self.body = content
    