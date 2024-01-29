# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionNote(object):

    """Implementation of the 'Subscription Note' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        body (str): TODO: type description here.
        subscription_id (int): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
        sticky (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "body": 'body',
        "subscription_id": 'subscription_id',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "sticky": 'sticky'
    }

    _optionals = [
        'id',
        'body',
        'subscription_id',
        'created_at',
        'updated_at',
        'sticky',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 body=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 sticky=APIHelper.SKIP):
        """Constructor for the SubscriptionNote class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if body is not APIHelper.SKIP:
            self.body = body 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if sticky is not APIHelper.SKIP:
            self.sticky = sticky 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        body = dictionary.get("body") if dictionary.get("body") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        sticky = dictionary.get("sticky") if "sticky" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   body,
                   subscription_id,
                   created_at,
                   updated_at,
                   sticky)
