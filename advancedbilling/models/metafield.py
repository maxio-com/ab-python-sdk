# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metafield_scope import MetafieldScope


class Metafield(object):

    """Implementation of the 'Metafield' model.

    TODO: type model description here.

    Attributes:
        id (float): TODO: type description here.
        name (str): TODO: type description here.
        scope (MetafieldScope): Warning: When updating a metafield's scope
            attribute, all scope attributes must be passed. Partially complete
            scope attributes will override the existing settings.
        data_count (int): the amount of subscriptions this metafield has been
            applied to in Chargify
        input_type (str): TODO: type description here.
        enum (List[List[str]] | None): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "scope": 'scope',
        "data_count": 'data_count',
        "input_type": 'input_type',
        "enum": 'enum'
    }

    _optionals = [
        'id',
        'name',
        'scope',
        'data_count',
        'input_type',
        'enum',
    ]

    _nullables = [
        'enum',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 scope=APIHelper.SKIP,
                 data_count=APIHelper.SKIP,
                 input_type=APIHelper.SKIP,
                 enum=APIHelper.SKIP):
        """Constructor for the Metafield class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if scope is not APIHelper.SKIP:
            self.scope = scope 
        if data_count is not APIHelper.SKIP:
            self.data_count = data_count 
        if input_type is not APIHelper.SKIP:
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        scope = MetafieldScope.from_dictionary(dictionary.get('scope')) if 'scope' in dictionary.keys() else APIHelper.SKIP
        data_count = dictionary.get("data_count") if dictionary.get("data_count") else APIHelper.SKIP
        input_type = dictionary.get("input_type") if dictionary.get("input_type") else APIHelper.SKIP
        if 'enum' in dictionary.keys():
            enum = APIHelper.deserialize_union_type(UnionTypeLookUp.get('MetafieldEnum'), dictionary.get('enum'), False) if dictionary.get('enum') is not None else None
        else:
            enum = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   scope,
                   data_count,
                   input_type,
                   enum)
