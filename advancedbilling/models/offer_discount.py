# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class OfferDiscount(object):

    """Implementation of the 'Offer Discount' model.

    TODO: type model description here.

    Attributes:
        coupon_code (str): TODO: type description here.
        coupon_id (int): TODO: type description here.
        coupon_name (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "coupon_code": 'coupon_code',
        "coupon_id": 'coupon_id',
        "coupon_name": 'coupon_name'
    }

    _optionals = [
        'coupon_code',
        'coupon_id',
        'coupon_name',
    ]

    def __init__(self,
                 coupon_code=APIHelper.SKIP,
                 coupon_id=APIHelper.SKIP,
                 coupon_name=APIHelper.SKIP):
        """Constructor for the OfferDiscount class"""

        # Initialize members of the class
        if coupon_code is not APIHelper.SKIP:
            self.coupon_code = coupon_code 
        if coupon_id is not APIHelper.SKIP:
            self.coupon_id = coupon_id 
        if coupon_name is not APIHelper.SKIP:
            self.coupon_name = coupon_name 

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
        coupon_code = dictionary.get("coupon_code") if dictionary.get("coupon_code") else APIHelper.SKIP
        coupon_id = dictionary.get("coupon_id") if dictionary.get("coupon_id") else APIHelper.SKIP
        coupon_name = dictionary.get("coupon_name") if dictionary.get("coupon_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(coupon_code,
                   coupon_id,
                   coupon_name)
