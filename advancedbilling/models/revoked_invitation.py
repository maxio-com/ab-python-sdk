# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RevokedInvitation(object):

    """Implementation of the 'Revoked Invitation' model.

    TODO: type model description here.

    Attributes:
        last_sent_at (str): TODO: type description here.
        last_accepted_at (str): TODO: type description here.
        uninvited_count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_sent_at": 'last_sent_at',
        "last_accepted_at": 'last_accepted_at',
        "uninvited_count": 'uninvited_count'
    }

    _optionals = [
        'last_sent_at',
        'last_accepted_at',
        'uninvited_count',
    ]

    def __init__(self,
                 last_sent_at=APIHelper.SKIP,
                 last_accepted_at=APIHelper.SKIP,
                 uninvited_count=APIHelper.SKIP):
        """Constructor for the RevokedInvitation class"""

        # Initialize members of the class
        if last_sent_at is not APIHelper.SKIP:
            self.last_sent_at = last_sent_at 
        if last_accepted_at is not APIHelper.SKIP:
            self.last_accepted_at = last_accepted_at 
        if uninvited_count is not APIHelper.SKIP:
            self.uninvited_count = uninvited_count 

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
        last_sent_at = dictionary.get("last_sent_at") if dictionary.get("last_sent_at") else APIHelper.SKIP
        last_accepted_at = dictionary.get("last_accepted_at") if dictionary.get("last_accepted_at") else APIHelper.SKIP
        uninvited_count = dictionary.get("uninvited_count") if dictionary.get("uninvited_count") else APIHelper.SKIP
        # Return an object of this model
        return cls(last_sent_at,
                   last_accepted_at,
                   uninvited_count)
