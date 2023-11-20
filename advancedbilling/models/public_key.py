# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PublicKey(object):

    """Implementation of the 'Public Key' model.

    TODO: type model description here.

    Attributes:
        public_key (str): TODO: type description here.
        requires_security_token (bool): TODO: type description here.
        created_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "public_key": 'public_key',
        "requires_security_token": 'requires_security_token',
        "created_at": 'created_at'
    }

    _optionals = [
        'public_key',
        'requires_security_token',
        'created_at',
    ]

    def __init__(self,
                 public_key=APIHelper.SKIP,
                 requires_security_token=APIHelper.SKIP,
                 created_at=APIHelper.SKIP):
        """Constructor for the PublicKey class"""

        # Initialize members of the class
        if public_key is not APIHelper.SKIP:
            self.public_key = public_key 
        if requires_security_token is not APIHelper.SKIP:
            self.requires_security_token = requires_security_token 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 

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
        public_key = dictionary.get("public_key") if dictionary.get("public_key") else APIHelper.SKIP
        requires_security_token = dictionary.get("requires_security_token") if "requires_security_token" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(public_key,
                   requires_security_token,
                   created_at)
