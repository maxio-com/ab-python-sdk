# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateProductCurrencyPrice(object):

    """Implementation of the 'Create Product Currency Price' model.

    TODO: type model description here.

    Attributes:
        currency (str): ISO code for one of the site level currencies.
        price (int): Price for the given role.
        role (CurrencyPriceRole): Role for the price.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "price": 'price',
        "role": 'role'
    }

    def __init__(self,
                 currency=None,
                 price=None,
                 role=None,
                 additional_properties={}):
        """Constructor for the CreateProductCurrencyPrice class"""

        # Initialize members of the class
        self.currency = currency 
        self.price = price 
        self.role = role 

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
        currency = dictionary.get("currency") if dictionary.get("currency") else None
        price = dictionary.get("price") if dictionary.get("price") else None
        role = dictionary.get("role") if dictionary.get("role") else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(currency,
                   price,
                   role,
                   dictionary)
