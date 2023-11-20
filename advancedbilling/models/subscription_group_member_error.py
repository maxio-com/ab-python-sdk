# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupMemberError(object):

    """Implementation of the 'Subscription Group Member Error' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        mtype (str): TODO: type description here.
        message (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "mtype": 'type',
        "message": 'message'
    }

    _optionals = [
        'id',
        'mtype',
        'message',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupMemberError class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   mtype,
                   message)
