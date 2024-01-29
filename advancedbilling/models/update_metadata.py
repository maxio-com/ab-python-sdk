# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateMetadata(object):

    """Implementation of the 'Update Metadata' model.

    TODO: type model description here.

    Attributes:
        current_name (str): TODO: type description here.
        name (str): TODO: type description here.
        value (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_name": 'current_name',
        "name": 'name',
        "value": 'value'
    }

    _optionals = [
        'current_name',
        'name',
        'value',
    ]

    def __init__(self,
                 current_name=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP):
        """Constructor for the UpdateMetadata class"""

        # Initialize members of the class
        if current_name is not APIHelper.SKIP:
            self.current_name = current_name 
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 

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
        current_name = dictionary.get("current_name") if dictionary.get("current_name") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        # Return an object of this model
        return cls(current_name,
                   name,
                   value)
