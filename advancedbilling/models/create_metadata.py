# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateMetadata(object):

    """Implementation of the 'Create Metadata' model.

    Attributes:
        name (str): The model property of type str.
        value (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the CreateMetadata class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   value,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'value={(self.value if hasattr(self, "value") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'value={(self.value if hasattr(self, "value") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
