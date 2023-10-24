# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateProductFamily(object):

    """Implementation of the 'Create Product Family' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        description (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "description": 'description'
    }

    _optionals = [
        'name',
        'description',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the CreateProductFamily class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   description)
