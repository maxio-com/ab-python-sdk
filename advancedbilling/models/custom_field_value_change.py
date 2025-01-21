# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomFieldValueChange(object):

    """Implementation of the 'Custom Field Value Change' model.

    Attributes:
        event_type (str): The model property of type str.
        metafield_name (str): The model property of type str.
        metafield_id (int): The model property of type int.
        old_value (str): The model property of type str.
        new_value (str): The model property of type str.
        resource_type (str): The model property of type str.
        resource_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event_type": 'event_type',
        "metafield_name": 'metafield_name',
        "metafield_id": 'metafield_id',
        "old_value": 'old_value',
        "new_value": 'new_value',
        "resource_type": 'resource_type',
        "resource_id": 'resource_id'
    }

    _nullables = [
        'old_value',
        'new_value',
    ]

    def __init__(self,
                 event_type=None,
                 metafield_name=None,
                 metafield_id=None,
                 old_value=None,
                 new_value=None,
                 resource_type=None,
                 resource_id=None,
                 additional_properties=None):
        """Constructor for the CustomFieldValueChange class"""

        # Initialize members of the class
        self.event_type = event_type 
        self.metafield_name = metafield_name 
        self.metafield_id = metafield_id 
        self.old_value = old_value 
        self.new_value = new_value 
        self.resource_type = resource_type 
        self.resource_id = resource_id 

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
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else None
        metafield_name = dictionary.get("metafield_name") if dictionary.get("metafield_name") else None
        metafield_id = dictionary.get("metafield_id") if dictionary.get("metafield_id") else None
        old_value = dictionary.get("old_value") if dictionary.get("old_value") else None
        new_value = dictionary.get("new_value") if dictionary.get("new_value") else None
        resource_type = dictionary.get("resource_type") if dictionary.get("resource_type") else None
        resource_id = dictionary.get("resource_id") if dictionary.get("resource_id") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(event_type,
                   metafield_name,
                   metafield_id,
                   old_value,
                   new_value,
                   resource_type,
                   resource_id,
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
            return APIHelper.is_valid_type(value=dictionary.event_type,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.metafield_name,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.metafield_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.old_value,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.new_value,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.resource_type,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.resource_id,
                                            type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('event_type'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('metafield_name'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('metafield_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('old_value'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('new_value'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('resource_type'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('resource_id'),
                                        type_callable=lambda value: isinstance(value, int))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'event_type={self.event_type!r}, '
                f'metafield_name={self.metafield_name!r}, '
                f'metafield_id={self.metafield_id!r}, '
                f'old_value={self.old_value!r}, '
                f'new_value={self.new_value!r}, '
                f'resource_type={self.resource_type!r}, '
                f'resource_id={self.resource_id!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'event_type={self.event_type!s}, '
                f'metafield_name={self.metafield_name!s}, '
                f'metafield_id={self.metafield_id!s}, '
                f'old_value={self.old_value!s}, '
                f'new_value={self.new_value!s}, '
                f'resource_type={self.resource_type!s}, '
                f'resource_id={self.resource_id!s}, '
                f'additional_properties={self.additional_properties!s})')
