# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class APIException(Exception):

    """Class that handles HTTP Exceptions when fetching API Endpoints.

    Attributes:
        response_code (int): The status code of the response.
        response (HttpResponse): The HttpResponse of the API call.

    """

    def __init__(self,
                 reason,
                 response):
        """Constructor for the APIException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(APIException, self).__init__(reason)
        self.reason = reason
        self.response = response
        self.response_code = response.status_code

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'status_code={self.response_code!s}, '
                f'message={self.reason!s})')
