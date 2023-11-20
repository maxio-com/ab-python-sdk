# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateUsage(object):

    """Implementation of the 'Create Usage' model.

    TODO: type model description here.

    Attributes:
        quantity (float): integer by default or decimal number if fractional
            quantities are enabled for the component
        price_point_id (str): TODO: type description here.
        memo (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": 'quantity',
        "price_point_id": 'price_point_id',
        "memo": 'memo'
    }

    _optionals = [
        'quantity',
        'price_point_id',
        'memo',
    ]

    def __init__(self,
                 quantity=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 memo=APIHelper.SKIP):
        """Constructor for the CreateUsage class"""

        # Initialize members of the class
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 

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
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        # Return an object of this model
        return cls(quantity,
                   price_point_id,
                   memo)
