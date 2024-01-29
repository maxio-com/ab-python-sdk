# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.coupon import Coupon


class CouponResponse(object):

    """Implementation of the 'Coupon Response' model.

    TODO: type model description here.

    Attributes:
        coupon (Coupon): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "coupon": 'coupon'
    }

    _optionals = [
        'coupon',
    ]

    def __init__(self,
                 coupon=APIHelper.SKIP):
        """Constructor for the CouponResponse class"""

        # Initialize members of the class
        if coupon is not APIHelper.SKIP:
            self.coupon = coupon 

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
        coupon = Coupon.from_dictionary(dictionary.get('coupon')) if 'coupon' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(coupon)
