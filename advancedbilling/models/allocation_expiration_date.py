# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AllocationExpirationDate(object):

    """Implementation of the 'Allocation Expiration Date' model.

    TODO: type model description here.

    Attributes:
        expires_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expires_at": 'expires_at'
    }

    _optionals = [
        'expires_at',
    ]

    def __init__(self,
                 expires_at=APIHelper.SKIP):
        """Constructor for the AllocationExpirationDate class"""

        # Initialize members of the class
        if expires_at is not APIHelper.SKIP:
            self.expires_at = expires_at 

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
        expires_at = dictionary.get("expires_at") if dictionary.get("expires_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(expires_at)
