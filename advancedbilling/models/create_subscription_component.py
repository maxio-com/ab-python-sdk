# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_custom_price import ComponentCustomPrice


class CreateSubscriptionComponent(object):

    """Implementation of the 'Create Subscription Component' model.

    Attributes:
        component_id (int | str | None): The model property of type int | str
            | None.
        enabled (bool): Used for on/off components only.
        unit_balance (int): Used for metered and events based components.
        allocated_quantity (int | str | None): Used for quantity based
            components.
        quantity (int): Deprecated. Use `allocated_quantity` instead.
        price_point_id (int | str | None): The model property of type int |
            str | None.
        custom_price (ComponentCustomPrice): Create or update custom pricing
            unique to the subscription. Used in place of `price_point_id`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "enabled": 'enabled',
        "unit_balance": 'unit_balance',
        "allocated_quantity": 'allocated_quantity',
        "quantity": 'quantity',
        "price_point_id": 'price_point_id',
        "custom_price": 'custom_price'
    }

    _optionals = [
        'component_id',
        'enabled',
        'unit_balance',
        'allocated_quantity',
        'quantity',
        'price_point_id',
        'custom_price',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 unit_balance=APIHelper.SKIP,
                 allocated_quantity=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateSubscriptionComponent class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if unit_balance is not APIHelper.SKIP:
            self.unit_balance = unit_balance 
        if allocated_quantity is not APIHelper.SKIP:
            self.allocated_quantity = allocated_quantity 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        component_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionComponentComponentId'), dictionary.get('component_id'), False) if dictionary.get('component_id') is not None else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        unit_balance = dictionary.get("unit_balance") if dictionary.get("unit_balance") else APIHelper.SKIP
        allocated_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionComponentAllocatedQuantity'), dictionary.get('allocated_quantity'), False) if dictionary.get('allocated_quantity') is not None else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionComponentPricePointId'), dictionary.get('price_point_id'), False) if dictionary.get('price_point_id') is not None else APIHelper.SKIP
        custom_price = ComponentCustomPrice.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   enabled,
                   unit_balance,
                   allocated_quantity,
                   quantity,
                   price_point_id,
                   custom_price,
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
                f'component_id={self.component_id!r}, '
                f'enabled={self.enabled!r}, '
                f'unit_balance={self.unit_balance!r}, '
                f'allocated_quantity={self.allocated_quantity!r}, '
                f'quantity={self.quantity!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'custom_price={self.custom_price!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={self.component_id!s}, '
                f'enabled={self.enabled!s}, '
                f'unit_balance={self.unit_balance!s}, '
                f'allocated_quantity={self.allocated_quantity!s}, '
                f'quantity={self.quantity!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'custom_price={self.custom_price!s}, '
                f'additional_properties={self.additional_properties!s})')
