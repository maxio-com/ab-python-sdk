# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Usage(object):

    """Implementation of the 'Usage' model.

    Attributes:
        id (int): The model property of type int.
        memo (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        price_point_id (int): The model property of type int.
        quantity (int | str | None): The model property of type int | str |
            None.
        overage_quantity (int): The model property of type int.
        component_id (int): The model property of type int.
        component_handle (str): The model property of type str.
        subscription_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "memo": 'memo',
        "created_at": 'created_at',
        "price_point_id": 'price_point_id',
        "quantity": 'quantity',
        "overage_quantity": 'overage_quantity',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "subscription_id": 'subscription_id'
    }

    _optionals = [
        'id',
        'memo',
        'created_at',
        'price_point_id',
        'quantity',
        'overage_quantity',
        'component_id',
        'component_handle',
        'subscription_id',
    ]

    _nullables = [
        'memo',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 overage_quantity=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Usage class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if overage_quantity is not APIHelper.SKIP:
            self.overage_quantity = overage_quantity 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('UsageQuantity'), dictionary.get('quantity'), False) if dictionary.get('quantity') is not None else APIHelper.SKIP
        overage_quantity = dictionary.get("overage_quantity") if dictionary.get("overage_quantity") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if dictionary.get("component_handle") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   memo,
                   created_at,
                   price_point_id,
                   quantity,
                   overage_quantity,
                   component_id,
                   component_handle,
                   subscription_id,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'overage_quantity={(self.overage_quantity if hasattr(self, "overage_quantity") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'overage_quantity={(self.overage_quantity if hasattr(self, "overage_quantity") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
