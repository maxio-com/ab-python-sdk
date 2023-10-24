# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CouponCurrency(object):

    """Implementation of the 'Coupon Currency' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        currency (str): TODO: type description here.
        price (int): TODO: type description here.
        coupon_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "currency": 'currency',
        "price": 'price',
        "coupon_id": 'coupon_id'
    }

    _optionals = [
        'id',
        'currency',
        'price',
        'coupon_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 coupon_id=APIHelper.SKIP):
        """Constructor for the CouponCurrency class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if price is not APIHelper.SKIP:
            self.price = price 
        if coupon_id is not APIHelper.SKIP:
            self.coupon_id = coupon_id 

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
        coupon_id = dictionary.get("coupon_id") if dictionary.get("coupon_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   currency,
                   price,
                   coupon_id)
