# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_component_custom_price import SubscriptionGroupComponentCustomPrice


class SubscriptionGroupSignupComponent(object):

    """Implementation of the 'Subscription Group Signup Component' model.

    Attributes:
        component_id (str | int | None): Required if passing any component to
            `components` attribute.
        allocated_quantity (str | int | None): The model property of type str
            | int | None.
        unit_balance (str | int | None): The model property of type str | int
            | None.
        price_point_id (str | int | None): The model property of type str |
            int | None.
        custom_price (SubscriptionGroupComponentCustomPrice): Used in place of
            `price_point_id` to define a custom price point unique to the
            subscription. You still need to provide `component_id`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "allocated_quantity": 'allocated_quantity',
        "unit_balance": 'unit_balance',
        "price_point_id": 'price_point_id',
        "custom_price": 'custom_price'
    }

    _optionals = [
        'component_id',
        'allocated_quantity',
        'unit_balance',
        'price_point_id',
        'custom_price',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 allocated_quantity=APIHelper.SKIP,
                 unit_balance=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupSignupComponent class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if allocated_quantity is not APIHelper.SKIP:
            self.allocated_quantity = allocated_quantity 
        if unit_balance is not APIHelper.SKIP:
            self.unit_balance = unit_balance 
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
        component_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupSignupComponentComponentId'), dictionary.get('component_id'), False) if dictionary.get('component_id') is not None else APIHelper.SKIP
        allocated_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupSignupComponentAllocatedQuantity'), dictionary.get('allocated_quantity'), False) if dictionary.get('allocated_quantity') is not None else APIHelper.SKIP
        unit_balance = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupSignupComponentUnitBalance'), dictionary.get('unit_balance'), False) if dictionary.get('unit_balance') is not None else APIHelper.SKIP
        price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupSignupComponentPricePointId'), dictionary.get('price_point_id'), False) if dictionary.get('price_point_id') is not None else APIHelper.SKIP
        custom_price = SubscriptionGroupComponentCustomPrice.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   allocated_quantity,
                   unit_balance,
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
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'allocated_quantity={(self.allocated_quantity if hasattr(self, "allocated_quantity") else None)!r}, '
                f'unit_balance={(self.unit_balance if hasattr(self, "unit_balance") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'custom_price={(self.custom_price if hasattr(self, "custom_price") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'allocated_quantity={(self.allocated_quantity if hasattr(self, "allocated_quantity") else None)!s}, '
                f'unit_balance={(self.unit_balance if hasattr(self, "unit_balance") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'custom_price={(self.custom_price if hasattr(self, "custom_price") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
