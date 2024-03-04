# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateMetadata(object):

    """Implementation of the 'Create Metadata' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        value (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "value": 'value'
    }

    _optionals = [
        'name',
        'value',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreateMetadata class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   value,
                   dictionary)
