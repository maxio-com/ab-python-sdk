# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProductPricePointCurrencyPrice(object):

    """Implementation of the 'Product Price Point Currency Price' model.

    object Product Price Point Currency Price:

    Attributes:
        id (int): TODO: type description here.
        currency (str): TODO: type description here.
        price (int): TODO: type description here.
        formatted_price (str): TODO: type description here.
        product_price_point_id (int): TODO: type description here.
        role (CurrencyPriceRole): Role for the price.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "currency": 'currency',
        "price": 'price',
        "formatted_price": 'formatted_price',
        "product_price_point_id": 'product_price_point_id',
        "role": 'role'
    }

    _optionals = [
        'id',
        'currency',
        'price',
        'formatted_price',
        'product_price_point_id',
        'role',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 formatted_price=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 role=APIHelper.SKIP):
        """Constructor for the ProductPricePointCurrencyPrice class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if price is not APIHelper.SKIP:
            self.price = price 
        if formatted_price is not APIHelper.SKIP:
            self.formatted_price = formatted_price 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if role is not APIHelper.SKIP:
            self.role = role 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        price = dictionary.get("price") if dictionary.get("price") else APIHelper.SKIP
        formatted_price = dictionary.get("formatted_price") if dictionary.get("formatted_price") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   currency,
                   price,
                   formatted_price,
                   product_price_point_id,
                   role)
