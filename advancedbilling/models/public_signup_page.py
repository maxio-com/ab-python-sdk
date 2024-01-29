# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PublicSignupPage(object):

    """Implementation of the 'Public Signup Page' model.

    TODO: type model description here.

    Attributes:
        id (int): The id of the signup page (public_signup_pages only)
        return_url (str): The url to which a customer will be returned after a
            successful signup (public_signup_pages only)
        return_params (str): The params to be appended to the return_url
            (public_signup_pages only)
        url (str): The url where the signup page can be viewed
            (public_signup_pages only)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "return_url": 'return_url',
        "return_params": 'return_params',
        "url": 'url'
    }

    _optionals = [
        'id',
        'return_url',
        'return_params',
        'url',
    ]

    _nullables = [
        'return_url',
        'return_params',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 return_url=APIHelper.SKIP,
                 return_params=APIHelper.SKIP,
                 url=APIHelper.SKIP):
        """Constructor for the PublicSignupPage class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
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
        return_url = dictionary.get("return_url") if "return_url" in dictionary.keys() else APIHelper.SKIP
        return_params = dictionary.get("return_params") if "return_params" in dictionary.keys() else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   return_url,
                   return_params,
                   url)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
