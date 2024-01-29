# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomFieldValueChange(object):

    """Implementation of the 'Custom Field Value Change' model.

    TODO: type model description here.

    Attributes:
        event_type (str): TODO: type description here.
        metafield_name (str): TODO: type description here.
        metafield_id (int): TODO: type description here.
        old_value (str): TODO: type description here.
        new_value (str): TODO: type description here.
        resource_type (str): TODO: type description here.
        resource_id (int): TODO: type description here.

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
                 resource_id=None):
        """Constructor for the CustomFieldValueChange class"""

        # Initialize members of the class
        self.event_type = event_type 
        self.metafield_name = metafield_name 
        self.metafield_id = metafield_id 
        self.old_value = old_value 
        self.new_value = new_value 
        self.resource_type = resource_type 
        self.resource_id = resource_id 

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
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else None
        metafield_name = dictionary.get("metafield_name") if dictionary.get("metafield_name") else None
        metafield_id = dictionary.get("metafield_id") if dictionary.get("metafield_id") else None
        old_value = dictionary.get("old_value") if dictionary.get("old_value") else None
        new_value = dictionary.get("new_value") if dictionary.get("new_value") else None
        resource_type = dictionary.get("resource_type") if dictionary.get("resource_type") else None
        resource_id = dictionary.get("resource_id") if dictionary.get("resource_id") else None
        # Return an object of this model
        return cls(event_type,
                   metafield_name,
                   metafield_id,
                   old_value,
                   new_value,
                   resource_type,
                   resource_id)

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
            return APIHelper.is_valid_type(value=dictionary.event_type, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.metafield_name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.metafield_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.old_value, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.new_value, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.resource_type, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.resource_id, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('event_type'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('metafield_name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('metafield_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('old_value'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('new_value'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('resource_type'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('resource_id'), type_callable=lambda value: isinstance(value, int))
