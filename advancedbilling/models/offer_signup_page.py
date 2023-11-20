# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class OfferSignupPage(object):

    """Implementation of the 'Offer Signup Page' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        nickname (str): TODO: type description here.
        enabled (bool): TODO: type description here.
        return_url (str): TODO: type description here.
        return_params (str): TODO: type description here.
        url (str): TODO: type description here.

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
                 url=APIHelper.SKIP):
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
        nickname = dictionary.get("nickname") if dictionary.get("nickname") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        return_url = dictionary.get("return_url") if dictionary.get("return_url") else APIHelper.SKIP
        return_params = dictionary.get("return_params") if dictionary.get("return_params") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   nickname,
                   enabled,
                   return_url,
                   return_params,
                   url)
