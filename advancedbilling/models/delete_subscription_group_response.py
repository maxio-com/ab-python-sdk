# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DeleteSubscriptionGroupResponse(object):

    """Implementation of the 'Delete Subscription Group Response' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        deleted (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "deleted": 'deleted'
    }

    _optionals = [
        'uid',
        'deleted',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 deleted=APIHelper.SKIP):
        """Constructor for the DeleteSubscriptionGroupResponse class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   deleted)
