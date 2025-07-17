# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateReasonCode(object):

    """Implementation of the 'Create Reason Code' model.

    Attributes:
        code (str): The unique identifier for the ReasonCode
        description (str): The friendly summary of what the code signifies
        position (int): The order that code appears in lists
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "description": 'description',
        "position": 'position'
    }

    _optionals = [
        'position',
    ]

    def __init__(self,
                 code=None,
                 description=None,
                 position=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateReasonCode class"""

        # Initialize members of the class
        self.code = code 
        self.description = description 
        if position is not APIHelper.SKIP:
            self.position = position 

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
        code = dictionary.get("code") if dictionary.get("code") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        position = dictionary.get("position") if dictionary.get("position") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(code,
                   description,
                   position,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!r}, '
                f'description={self.description!r}, '
                f'position={(self.position if hasattr(self, "position") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!s}, '
                f'description={self.description!s}, '
                f'position={(self.position if hasattr(self, "position") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
