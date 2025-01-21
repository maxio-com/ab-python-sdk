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

    Attributes:
        product_id (int): The model property of type int.
        component_id (int): For Product (or "baseline") line items, this field
            will have a value of `0`.
        price_point_id (int): The model property of type int.
        name (str): The model property of type str.
        mrr (int): The model property of type int.
        mrr_movements (List[MRRMovement]): The model property of type
            List[MRRMovement].
        quantity (int): The model property of type int.
        prev_quantity (int): The model property of type int.
        recurring (bool): When `true`, the line item's MRR value will
            contribute to the `plan` breakout. When `false`, the line item
            contributes to the `usage` breakout.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 recurring=APIHelper.SKIP,
                 additional_properties=None):
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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(product_id,
                   component_id,
                   price_point_id,
                   name,
                   mrr,
                   mrr_movements,
                   quantity,
                   prev_quantity,
                   recurring,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_id={self.product_id!r}, '
                f'component_id={self.component_id!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'name={self.name!r}, '
                f'mrr={self.mrr!r}, '
                f'mrr_movements={self.mrr_movements!r}, '
                f'quantity={self.quantity!r}, '
                f'prev_quantity={self.prev_quantity!r}, '
                f'recurring={self.recurring!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_id={self.product_id!s}, '
                f'component_id={self.component_id!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'name={self.name!s}, '
                f'mrr={self.mrr!s}, '
                f'mrr_movements={self.mrr_movements!s}, '
                f'quantity={self.quantity!s}, '
                f'prev_quantity={self.prev_quantity!s}, '
                f'recurring={self.recurring!s}, '
                f'additional_properties={self.additional_properties!s})')
