# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProductPricePointErrors(object):

    """Implementation of the 'Product Price Point Errors' model.

    TODO: type model description here.

    Attributes:
        price_point (str): TODO: type description here.
        interval (List[str]): TODO: type description here.
        interval_unit (List[str]): TODO: type description here.
        name (List[str]): TODO: type description here.
        price (List[str]): TODO: type description here.
        price_in_cents (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_point": 'price_point',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "name": 'name',
        "price": 'price',
        "price_in_cents": 'price_in_cents'
    }

    _optionals = [
        'price_point',
        'interval',
        'interval_unit',
        'name',
        'price',
        'price_in_cents',
    ]

    def __init__(self,
                 price_point=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP):
        """Constructor for the ProductPricePointErrors class"""

        # Initialize members of the class
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if name is not APIHelper.SKIP:
            self.name = name 
        if price is not APIHelper.SKIP:
            self.price = price 
        if price_in_cents is not APIHelper.SKIP:
            self.price_in_cents = price_in_cents 

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
        price_point = dictionary.get("price_point") if dictionary.get("price_point") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        price = dictionary.get("price") if dictionary.get("price") else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        # Return an object of this model
        return cls(price_point,
                   interval,
                   interval_unit,
                   name,
                   price,
                   price_in_cents)
