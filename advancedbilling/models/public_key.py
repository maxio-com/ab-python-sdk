# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PublicKey(object):

    """Implementation of the 'Public Key' model.

    Attributes:
        public_key (str): The model property of type str.
        requires_security_token (bool): The model property of type bool.
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the PublicKey class"""

        # Initialize members of the class
        if public_key is not APIHelper.SKIP:
            self.public_key = public_key 
        if requires_security_token is not APIHelper.SKIP:
            self.requires_security_token = requires_security_token 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        public_key = dictionary.get("public_key") if dictionary.get("public_key") else APIHelper.SKIP
        requires_security_token = dictionary.get("requires_security_token") if "requires_security_token" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(public_key,
                   requires_security_token,
                   created_at,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'public_key={self.public_key!r}, '
                f'requires_security_token={self.requires_security_token!r}, '
                f'created_at={self.created_at!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'public_key={self.public_key!s}, '
                f'requires_security_token={self.requires_security_token!s}, '
                f'created_at={self.created_at!s}, '
                f'additional_properties={self.additional_properties!s})')
