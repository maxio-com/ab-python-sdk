# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.item_price_point_data import ItemPricePointData


class ItemPricePointChanged(object):

    """Implementation of the 'Item Price Point Changed' model.

    TODO: type model description here.

    Attributes:
        item_id (int): TODO: type description here.
        item_type (str): TODO: type description here.
        item_handle (str): TODO: type description here.
        item_name (str): TODO: type description here.
        previous_price_point (ItemPricePointData): TODO: type description
            here.
        current_price_point (ItemPricePointData): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item_id": 'item_id',
        "item_type": 'item_type',
        "item_handle": 'item_handle',
        "item_name": 'item_name',
        "previous_price_point": 'previous_price_point',
        "current_price_point": 'current_price_point'
    }

    def __init__(self,
                 item_id=None,
                 item_type=None,
                 item_handle=None,
                 item_name=None,
                 previous_price_point=None,
                 current_price_point=None):
        """Constructor for the ItemPricePointChanged class"""

        # Initialize members of the class
        self.item_id = item_id 
        self.item_type = item_type 
        self.item_handle = item_handle 
        self.item_name = item_name 
        self.previous_price_point = previous_price_point 
        self.current_price_point = current_price_point 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        item_id = dictionary.get("item_id") if dictionary.get("item_id") else None
        item_type = dictionary.get("item_type") if dictionary.get("item_type") else None
        item_handle = dictionary.get("item_handle") if dictionary.get("item_handle") else None
        item_name = dictionary.get("item_name") if dictionary.get("item_name") else None
        previous_price_point = ItemPricePointData.from_dictionary(dictionary.get('previous_price_point')) if dictionary.get('previous_price_point') else None
        current_price_point = ItemPricePointData.from_dictionary(dictionary.get('current_price_point')) if dictionary.get('current_price_point') else None
        # Return an object of this model
        return cls(item_id,
                   item_type,
                   item_handle,
                   item_name,
                   previous_price_point,
                   current_price_point)

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
            return APIHelper.is_valid_type(value=dictionary.item_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.item_type, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.item_handle, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.item_name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.previous_price_point, type_callable=lambda value: ItemPricePointData.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.current_price_point, type_callable=lambda value: ItemPricePointData.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('item_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('item_type'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('item_handle'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('item_name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('previous_price_point'), type_callable=lambda value: ItemPricePointData.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_price_point'), type_callable=lambda value: ItemPricePointData.validate(value))
