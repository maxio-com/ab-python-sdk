# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.mrr_movement import MRRMovement


class MovementLineItem(object):

    """Implementation of the 'Movement Line Item' model.

    TODO: type model description here.

    Attributes:
        product_id (int): TODO: type description here.
        component_id (int): For Product (or "baseline") line items, this field
            will have a value of `0`.
        price_point_id (int): TODO: type description here.
        name (str): TODO: type description here.
        mrr (int): TODO: type description here.
        mrr_movements (List[MRRMovement]): TODO: type description here.
        quantity (int): TODO: type description here.
        prev_quantity (int): TODO: type description here.
        recurring (bool): When `true`, the line item's MRR value will
            contribute to the `plan` breakout. When `false`, the line item
            contributes to the `usage` breakout.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_id": 'product_id',
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "name": 'name',
        "mrr": 'mrr',
        "mrr_movements": 'mrr_movements',
        "quantity": 'quantity',
        "prev_quantity": 'prev_quantity',
        "recurring": 'recurring'
    }

    _optionals = [
        'product_id',
        'component_id',
        'price_point_id',
        'name',
        'mrr',
        'mrr_movements',
        'quantity',
        'prev_quantity',
        'recurring',
    ]

    def __init__(self,
                 product_id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 mrr=APIHelper.SKIP,
                 mrr_movements=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 prev_quantity=APIHelper.SKIP,
                 recurring=APIHelper.SKIP):
        """Constructor for the MovementLineItem class"""

        # Initialize members of the class
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if mrr is not APIHelper.SKIP:
            self.mrr = mrr 
        if mrr_movements is not APIHelper.SKIP:
            self.mrr_movements = mrr_movements 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if prev_quantity is not APIHelper.SKIP:
            self.prev_quantity = prev_quantity 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 

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
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        mrr = dictionary.get("mrr") if dictionary.get("mrr") else APIHelper.SKIP
        mrr_movements = None
        if dictionary.get('mrr_movements') is not None:
            mrr_movements = [MRRMovement.from_dictionary(x) for x in dictionary.get('mrr_movements')]
        else:
            mrr_movements = APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        prev_quantity = dictionary.get("prev_quantity") if dictionary.get("prev_quantity") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(product_id,
                   component_id,
                   price_point_id,
                   name,
                   mrr,
                   mrr_movements,
                   quantity,
                   prev_quantity,
                   recurring)
