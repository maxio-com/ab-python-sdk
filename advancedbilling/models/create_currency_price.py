# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateCurrencyPrice(object):

    """Implementation of the 'Create Currency Price' model.

    TODO: type model description here.

    Attributes:
        currency (str): ISO code for a currency defined on the site level
        price (float): Price for the price level in this currency
        price_id (int): ID of the price that this corresponds with

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "price": 'price',
        "price_id": 'price_id'
    }

    _optionals = [
        'currency',
        'price',
        'price_id',
    ]

    def __init__(self,
                 currency=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 price_id=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreateCurrencyPrice class"""

        # Initialize members of the class
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if price is not APIHelper.SKIP:
            self.price = price 
        if price_id is not APIHelper.SKIP:
            self.price_id = price_id 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        price = dictionary.get("price") if dictionary.get("price") else APIHelper.SKIP
        price_id = dictionary.get("price_id") if dictionary.get("price_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(currency,
                   price,
                   price_id,
                   dictionary)
