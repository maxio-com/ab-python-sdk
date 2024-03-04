# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListSubscriptionGroupsMeta(object):

    """Implementation of the 'List Subscription Groups Meta' model.

    TODO: type model description here.

    Attributes:
        current_page (int): TODO: type description here.
        total_count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_page": 'current_page',
        "total_count": 'total_count'
    }

    _optionals = [
        'current_page',
        'total_count',
    ]

    def __init__(self,
                 current_page=APIHelper.SKIP,
                 total_count=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListSubscriptionGroupsMeta class"""

        # Initialize members of the class
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        current_page = dictionary.get("current_page") if dictionary.get("current_page") else APIHelper.SKIP
        total_count = dictionary.get("total_count") if dictionary.get("total_count") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(current_page,
                   total_count,
                   dictionary)
