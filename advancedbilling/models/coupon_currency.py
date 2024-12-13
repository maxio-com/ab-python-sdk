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
        price (float): TODO: type description here.
        coupon_id (int): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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

    _nullables = [
        'id',
        'price',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 coupon_id=APIHelper.SKIP,
                 additional_properties=None):
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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        price = dictionary.get("price") if "price" in dictionary.keys() else APIHelper.SKIP
        coupon_id = dictionary.get("coupon_id") if dictionary.get("coupon_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   currency,
                   price,
                   coupon_id,
                   additional_properties)
