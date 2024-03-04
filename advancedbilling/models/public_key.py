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
        created_at (datetime): TODO: type description here.

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
                 created_at=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the PublicKey class"""

        # Initialize members of the class
        if public_key is not APIHelper.SKIP:
            self.public_key = public_key 
        if requires_security_token is not APIHelper.SKIP:
            self.requires_security_token = requires_security_token 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

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
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(public_key,
                   requires_security_token,
                   created_at,
                   dictionary)
