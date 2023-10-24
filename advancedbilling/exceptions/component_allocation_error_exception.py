# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
import advancedbilling.exceptions.api_exception
from advancedbilling.models.component_allocation_error_item import ComponentAllocationErrorItem


class ComponentAllocationErrorException(advancedbilling.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ComponentAllocationErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ComponentAllocationErrorException, self).__init__(reason, response)
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
        self.errors = None
        if dictionary.get('errors') is not None:
            self.errors = [ComponentAllocationErrorItem.from_dictionary(x) for x in dictionary.get('errors')]
        else:
            self.errors = None
