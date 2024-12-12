# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Metadata(object):

    """Implementation of the 'Metadata' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        value (str): TODO: type description here.
        resource_id (int): TODO: type description here.
        name (str): TODO: type description here.
        deleted_at (datetime): TODO: type description here.
        metafield_id (int): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "value": 'value',
        "resource_id": 'resource_id',
        "name": 'name',
        "deleted_at": 'deleted_at',
        "metafield_id": 'metafield_id'
    }

    _optionals = [
        'id',
        'value',
        'resource_id',
        'name',
        'deleted_at',
        'metafield_id',
    ]

    _nullables = [
        'id',
        'value',
        'resource_id',
        'deleted_at',
        'metafield_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 resource_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP,
                 metafield_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Metadata class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if value is not APIHelper.SKIP:
            self.value = value 
        if resource_id is not APIHelper.SKIP:
            self.resource_id = resource_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 
        if metafield_id is not APIHelper.SKIP:
            self.metafield_id = metafield_id 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        value = dictionary.get("value") if "value" in dictionary.keys() else APIHelper.SKIP
        resource_id = dictionary.get("resource_id") if "resource_id" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        metafield_id = dictionary.get("metafield_id") if "metafield_id" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   value,
                   resource_id,
                   name,
                   deleted_at,
                   metafield_id,
                   additional_properties)
