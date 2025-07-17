# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class OfferSignupPage(object):

    """Implementation of the 'Offer Signup Page' model.

    Attributes:
        id (int): The model property of type int.
        nickname (str): The model property of type str.
        enabled (bool): The model property of type bool.
        return_url (str): The model property of type str.
        return_params (str): The model property of type str.
        url (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "nickname": 'nickname',
        "enabled": 'enabled',
        "return_url": 'return_url',
        "return_params": 'return_params',
        "url": 'url'
    }

    _optionals = [
        'id',
        'nickname',
        'enabled',
        'return_url',
        'return_params',
        'url',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 nickname=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 return_url=APIHelper.SKIP,
                 return_params=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OfferSignupPage class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if nickname is not APIHelper.SKIP:
            self.nickname = nickname 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if return_url is not APIHelper.SKIP:
            self.return_url = return_url 
        if return_params is not APIHelper.SKIP:
            self.return_params = return_params 
        if url is not APIHelper.SKIP:
            self.url = url 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        nickname = dictionary.get("nickname") if dictionary.get("nickname") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        return_url = dictionary.get("return_url") if dictionary.get("return_url") else APIHelper.SKIP
        return_params = dictionary.get("return_params") if dictionary.get("return_params") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   nickname,
                   enabled,
                   return_url,
                   return_params,
                   url,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'nickname={(self.nickname if hasattr(self, "nickname") else None)!r}, '
                f'enabled={(self.enabled if hasattr(self, "enabled") else None)!r}, '
                f'return_url={(self.return_url if hasattr(self, "return_url") else None)!r}, '
                f'return_params={(self.return_params if hasattr(self, "return_params") else None)!r}, '
                f'url={(self.url if hasattr(self, "url") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'nickname={(self.nickname if hasattr(self, "nickname") else None)!s}, '
                f'enabled={(self.enabled if hasattr(self, "enabled") else None)!s}, '
                f'return_url={(self.return_url if hasattr(self, "return_url") else None)!s}, '
                f'return_params={(self.return_params if hasattr(self, "return_params") else None)!s}, '
                f'url={(self.url if hasattr(self, "url") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
