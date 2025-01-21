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

    Attributes:
        item_id (int): The model property of type int.
        item_type (str): The model property of type str.
        item_handle (str): The model property of type str.
        item_name (str): The model property of type str.
        previous_price_point (ItemPricePointData): The model property of type
            ItemPricePointData.
        current_price_point (ItemPricePointData): The model property of type
            ItemPricePointData.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 current_price_point=None,
                 additional_properties=None):
        """Constructor for the ItemPricePointChanged class"""

        # Initialize members of the class
        self.item_id = item_id 
        self.item_type = item_type 
        self.item_handle = item_handle 
        self.item_name = item_name 
        self.previous_price_point = previous_price_point 
        self.current_price_point = current_price_point 

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
        item_id = dictionary.get("item_id") if dictionary.get("item_id") else None
        item_type = dictionary.get("item_type") if dictionary.get("item_type") else None
        item_handle = dictionary.get("item_handle") if dictionary.get("item_handle") else None
        item_name = dictionary.get("item_name") if dictionary.get("item_name") else None
        previous_price_point = ItemPricePointData.from_dictionary(dictionary.get('previous_price_point')) if dictionary.get('previous_price_point') else None
        current_price_point = ItemPricePointData.from_dictionary(dictionary.get('current_price_point')) if dictionary.get('current_price_point') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(item_id,
                   item_type,
                   item_handle,
                   item_name,
                   previous_price_point,
                   current_price_point,
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
            return APIHelper.is_valid_type(value=dictionary.item_id,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.item_type,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.item_handle,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.item_name,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.previous_price_point,
                                            type_callable=lambda value: ItemPricePointData.validate(value),
                                            is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.current_price_point,
                                            type_callable=lambda value: ItemPricePointData.validate(value),
                                            is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('item_id'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('item_type'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('item_handle'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('item_name'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('previous_price_point'),
                                        type_callable=lambda value: ItemPricePointData.validate(value),
                                        is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('current_price_point'),
                                        type_callable=lambda value: ItemPricePointData.validate(value),
                                        is_model_dict=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'item_id={self.item_id!r}, '
                f'item_type={self.item_type!r}, '
                f'item_handle={self.item_handle!r}, '
                f'item_name={self.item_name!r}, '
                f'previous_price_point={self.previous_price_point!r}, '
                f'current_price_point={self.current_price_point!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'item_id={self.item_id!s}, '
                f'item_type={self.item_type!s}, '
                f'item_handle={self.item_handle!s}, '
                f'item_name={self.item_name!s}, '
                f'previous_price_point={self.previous_price_point!s}, '
                f'current_price_point={self.current_price_point!s}, '
                f'additional_properties={self.additional_properties!s})')
