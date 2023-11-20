# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionComponentSubscription(object):

    """Implementation of the 'Subscription Component Subscription' model.

    An optional object, will be returned if provided `include=subscription`
    query param.

    Attributes:
        state (str): TODO: type description here.
        updated_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "state": 'state',
        "updated_at": 'updated_at'
    }

    _optionals = [
        'state',
        'updated_at',
    ]

    def __init__(self,
                 state=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP):
        """Constructor for the SubscriptionComponentSubscription class"""

        # Initialize members of the class
        if state is not APIHelper.SKIP:
            self.state = state 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 

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
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(state,
                   updated_at)
