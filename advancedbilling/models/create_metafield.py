# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metafield_scope import MetafieldScope


class CreateMetafield(object):

    """Implementation of the 'Create Metafield' model.

    Attributes:
        name (str): The model property of type str.
        scope (MetafieldScope): Warning: When updating a metafield's scope
            attribute, all scope attributes must be passed. Partially complete
            scope attributes will override the existing settings.
        input_type (MetafieldInput): Indicates how data should be added to the
            metafield. For example, a text type is just a string, so a given
            metafield of this type can have any value attached. On the other
            hand, dropdown and radio have a set of allowed values that can be
            input, and appear differently on a Public Signup Page. Defaults to
            'text'
        enum (List[str]): Only applicable when input_type is radio or
            dropdown. Empty strings will not be submitted.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "scope": 'scope',
        "input_type": 'input_type',
        "enum": 'enum'
    }

    _optionals = [
        'name',
        'scope',
        'input_type',
        'enum',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 scope=APIHelper.SKIP,
                 input_type=APIHelper.SKIP,
                 enum=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateMetafield class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if scope is not APIHelper.SKIP:
            self.scope = scope 
        if input_type is not APIHelper.SKIP:
            self.input_type = input_type 
        if enum is not APIHelper.SKIP:
            self.enum = enum 

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
        scope = MetafieldScope.from_dictionary(dictionary.get('scope')) if 'scope' in dictionary.keys() else APIHelper.SKIP
        input_type = dictionary.get("input_type") if dictionary.get("input_type") else APIHelper.SKIP
        enum = dictionary.get("enum") if dictionary.get("enum") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   scope,
                   input_type,
                   enum,
                   additional_properties)

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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'scope={(self.scope if hasattr(self, "scope") else None)!r}, '
                f'input_type={(self.input_type if hasattr(self, "input_type") else None)!r}, '
                f'enum={(self.enum if hasattr(self, "enum") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'scope={(self.scope if hasattr(self, "scope") else None)!s}, '
                f'input_type={(self.input_type if hasattr(self, "input_type") else None)!s}, '
                f'enum={(self.enum if hasattr(self, "enum") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
