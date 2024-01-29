# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentCurrencyPrice(object):

    """Implementation of the 'Component Currency Price' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        currency (str): TODO: type description here.
        price (str): TODO: type description here.
        formatted_price (str): TODO: type description here.
        price_id (int): TODO: type description here.
        price_point_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "currency": 'currency',
        "price": 'price',
        "formatted_price": 'formatted_price',
        "price_id": 'price_id',
        "price_point_id": 'price_point_id'
    }

    _optionals = [
        'id',
        'currency',
        'price',
        'formatted_price',
        'price_id',
        'price_point_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 formatted_price=APIHelper.SKIP,
                 price_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP):
        """Constructor for the ComponentCurrencyPrice class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if price is not APIHelper.SKIP:
            self.price = price 
        if formatted_price is not APIHelper.SKIP:
            self.formatted_price = formatted_price 
        if price_id is not APIHelper.SKIP:
            self.price_id = price_id 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        price = dictionary.get("price") if dictionary.get("price") else APIHelper.SKIP
        formatted_price = dictionary.get("formatted_price") if dictionary.get("formatted_price") else APIHelper.SKIP
        price_id = dictionary.get("price_id") if dictionary.get("price_id") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   currency,
                   price,
                   formatted_price,
                   price_id,
                   price_point_id)

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
