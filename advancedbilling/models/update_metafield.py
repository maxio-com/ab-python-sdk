# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metafield_scope import MetafieldScope


class UpdateMetafield(object):

    """Implementation of the 'Update Metafield' model.

    TODO: type model description here.

    Attributes:
        current_name (str): TODO: type description here.
        name (str): TODO: type description here.
        scope (MetafieldScope): Warning: When updating a metafield's scope
            attribute, all scope attributes must be passed. Partially complete
            scope attributes will override the existing settings.
        input_type (MetafieldInput): Indicates how data should be added to the
            metafield. For example, a text type is just a string, so a given
            metafield of this type can have any value attached. On the other
            hand, dropdown and radio have a set of allowed values that can be
            input, and appear differently on a Public Signup Page.
        enum (List[str]): Only applicable when input_type is radio or
            dropdown

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_name": 'current_name',
        "name": 'name',
        "scope": 'scope',
        "input_type": 'input_type',
        "enum": 'enum'
    }

    _optionals = [
        'current_name',
        'name',
        'scope',
        'input_type',
        'enum',
    ]

    def __init__(self,
                 current_name=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 scope=APIHelper.SKIP,
                 input_type='text',
                 enum=APIHelper.SKIP):
        """Constructor for the UpdateMetafield class"""

        # Initialize members of the class
        if current_name is not APIHelper.SKIP:
            self.current_name = current_name 
        if name is not APIHelper.SKIP:
            self.name = name 
        if scope is not APIHelper.SKIP:
            self.scope = scope 
        self.input_type = input_type 
        if enum is not APIHelper.SKIP:
            self.enum = enum 

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
        scope = MetafieldScope.from_dictionary(dictionary.get('scope')) if 'scope' in dictionary.keys() else APIHelper.SKIP
        input_type = dictionary.get("input_type") if dictionary.get("input_type") else 'text'
        enum = dictionary.get("enum") if dictionary.get("enum") else APIHelper.SKIP
        # Return an object of this model
        return cls(current_name,
                   name,
                   scope,
                   input_type,
                   enum)

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
