# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RenewalPreviewComponent(object):

    """Implementation of the 'Renewal Preview Component' model.

    TODO: type model description here.

    Attributes:
        component_id (str | int | None): Either the component's Chargify id or
            its handle prefixed with `handle:`
        quantity (int): The quantity for which you wish to preview billing.
            This is useful if you want to preview a predicted, higher usage
            value than is currently present on the subscription.  This
            quantity represents:  - Whether or not an on/off component is
            enabled - use 0 for disabled or 1 for enabled - The desired
            allocated_quantity for a quantity-based component - The desired
            unit_balance for a metered component - The desired metric quantity
            for an events-based component
        price_point_id (str | int | None): Either the component price point's
            Chargify id or its handle prefixed with `handle:`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "quantity": 'quantity',
        "price_point_id": 'price_point_id'
    }

    _optionals = [
        'component_id',
        'quantity',
        'price_point_id',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP):
        """Constructor for the RenewalPreviewComponent class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 

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
        component_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RenewalPreviewComponentComponentId'), dictionary.get('component_id'), False) if dictionary.get('component_id') is not None else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RenewalPreviewComponentPricePointId'), dictionary.get('price_point_id'), False) if dictionary.get('price_point_id') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(component_id,
                   quantity,
                   price_point_id)
