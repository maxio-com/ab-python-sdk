# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CouponSubcodes(object):

    """Implementation of the 'Coupon Subcodes' model.

    TODO: type model description here.

    Attributes:
        codes (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "codes": 'codes'
    }

    _optionals = [
        'codes',
    ]

    def __init__(self,
                 codes=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CouponSubcodes class"""

        # Initialize members of the class
        if codes is not APIHelper.SKIP:
            self.codes = codes 

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
        codes = dictionary.get("codes") if dictionary.get("codes") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(codes,
                   dictionary)
