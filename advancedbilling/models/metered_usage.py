# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class MeteredUsage(object):

    """Implementation of the 'Metered Usage' model.

    Attributes:
        previous_unit_balance (str): The model property of type str.
        new_unit_balance (int): The model property of type int.
        usage_quantity (int): The model property of type int.
        component_id (int): The model property of type int.
        component_handle (str): The model property of type str.
        memo (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_unit_balance": 'previous_unit_balance',
        "new_unit_balance": 'new_unit_balance',
        "usage_quantity": 'usage_quantity',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "memo": 'memo'
    }

    def __init__(self,
                 previous_unit_balance=None,
                 new_unit_balance=None,
                 usage_quantity=None,
                 component_id=None,
                 component_handle=None,
                 memo=None,
                 additional_properties=None):
        """Constructor for the MeteredUsage class"""

        # Initialize members of the class
        self.previous_unit_balance = previous_unit_balance 
        self.new_unit_balance = new_unit_balance 
        self.usage_quantity = usage_quantity 
        self.component_id = component_id 
        self.component_handle = component_handle 
        self.memo = memo 

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
        previous_unit_balance = dictionary.get("previous_unit_balance") if dictionary.get("previous_unit_balance") else None
        new_unit_balance = dictionary.get("new_unit_balance") if dictionary.get("new_unit_balance") else None
        usage_quantity = dictionary.get("usage_quantity") if dictionary.get("usage_quantity") else None
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else None
        component_handle = dictionary.get("component_handle") if dictionary.get("component_handle") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(previous_unit_balance,
                   new_unit_balance,
                   usage_quantity,
                   component_id,
                   component_handle,
                   memo,
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
            return APIHelper.is_valid_type(value=dictionary.previous_unit_balance,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.new_unit_balance,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.usage_quantity,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.component_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.component_handle,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.memo,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('previous_unit_balance'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('new_unit_balance'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('usage_quantity'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('component_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('component_handle'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'previous_unit_balance={self.previous_unit_balance!r}, '
                f'new_unit_balance={self.new_unit_balance!r}, '
                f'usage_quantity={self.usage_quantity!r}, '
                f'component_id={self.component_id!r}, '
                f'component_handle={self.component_handle!r}, '
                f'memo={self.memo!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'previous_unit_balance={self.previous_unit_balance!s}, '
                f'new_unit_balance={self.new_unit_balance!s}, '
                f'usage_quantity={self.usage_quantity!s}, '
                f'component_id={self.component_id!s}, '
                f'component_handle={self.component_handle!s}, '
                f'memo={self.memo!s}, '
                f'additional_properties={self.additional_properties!s})')
