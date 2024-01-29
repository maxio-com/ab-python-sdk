# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CountResponse(object):

    """Implementation of the 'Count Response' model.

    TODO: type model description here.

    Attributes:
        count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count'
    }

    _optionals = [
        'count',
    ]

    def __init__(self,
                 count=APIHelper.SKIP):
        """Constructor for the CountResponse class"""

        # Initialize members of the class
        if count is not APIHelper.SKIP:
            self.count = count 

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
        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        # Return an object of this model
        return cls(count)
