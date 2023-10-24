# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ItemPricePointData(object):

    """Implementation of the 'Item Price Point Data' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        handle (str): TODO: type description here.
        name (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "handle": 'handle',
        "name": 'name'
    }

    _optionals = [
        'id',
        'handle',
        'name',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the ItemPricePointData class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   handle,
                   name)

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
