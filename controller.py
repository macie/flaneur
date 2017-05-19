# -*- coding: utf-8 -*-
import inspect
from request import Request
from response import Response
from view import NotFoundView


class Controller(object):
    """
        Controller binds user actions (HTTP requests) with object views.
    """
    def __init__(self):
        self.cache = {}

    def __call__(self, environ, start_response):
        request = Request()
        request.method = environ.get('REQUEST_METHOD', 'GET')
        request.uri = environ.get('PATH_INFO', '/')
        if request.method == 'GET':
            request.body = environ.get('QUERY_STRING', '')
        elif request.method == 'POST':
            length = int(environ.get('CONTENT_LENGTH', '0'))
            request.body = environ['wsgi.input'].read(length).decode()

        for header in environ:
            if header.startswith('HTTP_'):
                request.headers[header[4:].capitalize()] = environ[header]

        view = self.dispatch(request.uri)
        method = getattr(view, request.method.lower(), 'get')
        response = method(view, request)

        start_response(
            '{} {}'.format(response.status, response.reason),
            list(response.headers.items())
        )
        return [response.body.encode('utf-8')]

    def discover(self):
        # package = []
        # for module in package:
        #     for view in module:
        #         sig = inspect.signature(view)
        #         for arg in sig.parameters.values():
        #             if arg.default == arg.empty:
        #                 self.cache['{}/<arg>'.format(view.__name__)] = view
        import view
        self.cache['/'] = view.View

    def dispatch(self, uri):
        if not self.cache:
            self.discover()
        return self.cache.get(uri, NotFoundView)

    def location(self):
        import inspect, os
        frame = inspect.stack()[-1]  # TODO: next frame after Controller
        path = os.path.join(os.getcwd(), frame.filename)

        return os.path.dirname(path)

    def response_with(self, response):
        return response if response else Response()
