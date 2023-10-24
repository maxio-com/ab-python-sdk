# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class TooManyManagementLinkRequests(object):

    """Implementation of the 'Too Many Management Link Requests' model.

    TODO: type model description here.

    Attributes:
        error (str): TODO: type description here.
        new_link_available_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'error',
        "new_link_available_at": 'new_link_available_at'
    }

    _optionals = [
        'error',
        'new_link_available_at',
    ]

    def __init__(self,
                 error=APIHelper.SKIP,
                 new_link_available_at=APIHelper.SKIP):
        """Constructor for the TooManyManagementLinkRequests class"""

        # Initialize members of the class
        if error is not APIHelper.SKIP:
            self.error = error 
        if new_link_available_at is not APIHelper.SKIP:
            self.new_link_available_at = APIHelper.apply_datetime_converter(new_link_available_at, APIHelper.RFC3339DateTime) if new_link_available_at else None 

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
        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        new_link_available_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("new_link_available_at")).datetime if dictionary.get("new_link_available_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(error,
                   new_link_available_at)
