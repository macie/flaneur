# -*- coding: utf-8 -*-
"""
    A view module.
"""
from response import Response

class View(object):
    """
        A View object.
    """
    def __init__(self):
        pass

    def delete(self, request):
        """
            HTTP DELETE method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

    def get(self, request):
        """
            HTTP GET method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

    def head(self, request):
        """
            HTTP HEAD method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

    def options(self, request):
        """
            HTTP OPTIONS method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

    def patch(self, request):
        """
            HTTP PATCH method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

    def post(self, request):
        """
            HTTP POST method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

    def put(self, request):
        """
            HTTP PUT method implementation.

            Args:
                request: A Request object.

            Returns:
                A string or Response object.
        """
        raise NotImplementedError

#pylint: disable=W0223

class NotFoundView(View):
    """
        Default view for status code 404 (Not Found).
    """
    def get(self, request):
        response = Response('Not Found :(')
        response.status = 404
        response.reason = 'Not Found'
        return response

class InternalServerErrorView(View):
    """
        Default view for status code 500 (Internal Server Error).
    """
    def get(self, request):
        response = Response('Internal Server Error')
        response.status = 500
        response.reason = 'Internal Server Error'
        return response
