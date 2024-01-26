# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Usage(object):

    """Implementation of the 'Usage' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        memo (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        price_point_id (int): TODO: type description here.
        quantity (int | str | None): TODO: type description here.
        overage_quantity (int): TODO: type description here.
        component_id (int): TODO: type description here.
        component_handle (str): TODO: type description here.
        subscription_id (int): TODO: type description here.

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

    def __init__(self,
                 id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 overage_quantity=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP):
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('UsageQuantity'), dictionary.get('quantity'), False) if dictionary.get('quantity') is not None else APIHelper.SKIP
        overage_quantity = dictionary.get("overage_quantity") if dictionary.get("overage_quantity") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if dictionary.get("component_handle") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   memo,
                   created_at,
                   price_point_id,
                   quantity,
                   overage_quantity,
                   component_id,
                   component_handle,
                   subscription_id)
