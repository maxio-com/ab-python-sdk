# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper
import maxioadvancedbillingformerlychargifyapi.exceptions.api_exception
from maxioadvancedbillingformerlychargifyapi.models.errors_1 import Errors1


class SubscriptionsActivateJson400ErrorException(maxioadvancedbillingformerlychargifyapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the SubscriptionsActivateJson400ErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(SubscriptionsActivateJson400ErrorException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.errors = Errors1.from_dictionary(dictionary.get('errors')) if 'errors' in dictionary.keys() else None
