# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DelayedCancellationResponse(object):

    """Implementation of the 'Delayed Cancellation Response' model.

    TODO: type model description here.

    Attributes:
        message (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message'
    }

    _optionals = [
        'message',
    ]

    def __init__(self,
                 message=APIHelper.SKIP):
        """Constructor for the DelayedCancellationResponse class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 

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
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(message)
