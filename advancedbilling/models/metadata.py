# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Metadata(object):

    """Implementation of the 'Metadata' model.

    Attributes:
        id (int): The model property of type int.
        value (str): The model property of type str.
        resource_id (int): The model property of type int.
        name (str): The model property of type str.
        deleted_at (datetime): The model property of type datetime.
        metafield_id (int): The model property of type int.
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'value={(self.value if hasattr(self, "value") else None)!r}, '
                f'resource_id={(self.resource_id if hasattr(self, "resource_id") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'deleted_at={(self.deleted_at if hasattr(self, "deleted_at") else None)!r}, '
                f'metafield_id={(self.metafield_id if hasattr(self, "metafield_id") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'value={(self.value if hasattr(self, "value") else None)!s}, '
                f'resource_id={(self.resource_id if hasattr(self, "resource_id") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'deleted_at={(self.deleted_at if hasattr(self, "deleted_at") else None)!s}, '
                f'metafield_id={(self.metafield_id if hasattr(self, "metafield_id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
