# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
import advancedbilling.exceptions.api_exception
from advancedbilling.models.proforma_error import ProformaError


class ProformaBadRequestErrorResponseException(advancedbilling.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ProformaBadRequestErrorResponseException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ProformaBadRequestErrorResponseException, self).__init__(reason, response)
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
        self.errors = ProformaError.from_dictionary(dictionary.get('errors')) if 'errors' in dictionary.keys() else None
