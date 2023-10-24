# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReplayWebhooksResponse(object):

    """Implementation of the 'Replay Webhooks Response' model.

    TODO: type model description here.

    Attributes:
        status (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status'
    }

    _optionals = [
        'status',
    ]

    def __init__(self,
                 status=APIHelper.SKIP):
        """Constructor for the ReplayWebhooksResponse class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 

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
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(status)
