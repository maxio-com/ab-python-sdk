# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateCouponCurrency(object):

    """Implementation of the 'Update Coupon Currency' model.

    TODO: type model description here.

    Attributes:
        currency (str): ISO code for the site defined currency.
        price (int): Price for the given currency.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "price": 'price'
    }

    def __init__(self,
                 currency=None,
                 price=None,
                 additional_properties={}):
        """Constructor for the UpdateCouponCurrency class"""

        # Initialize members of the class
        self.currency = currency 
        self.price = price 

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
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(currency,
                   price,
                   dictionary)
