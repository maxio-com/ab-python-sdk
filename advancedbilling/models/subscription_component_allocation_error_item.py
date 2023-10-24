# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionComponentAllocationErrorItem(object):

    """Implementation of the 'Subscription Component Allocation Error Item' model.

    TODO: type model description here.

    Attributes:
        kind (str): TODO: type description here.
        message (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kind": 'kind',
        "message": 'message'
    }

    _optionals = [
        'kind',
        'message',
    ]

    def __init__(self,
                 kind=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the SubscriptionComponentAllocationErrorItem class"""

        # Initialize members of the class
        if kind is not APIHelper.SKIP:
            self.kind = kind 
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
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(kind,
                   message)
