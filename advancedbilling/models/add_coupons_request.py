# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AddCouponsRequest(object):

    """Implementation of the 'Add Coupons Request' model.

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
                 codes=APIHelper.SKIP):
        """Constructor for the AddCouponsRequest class"""

        # Initialize members of the class
        if codes is not APIHelper.SKIP:
            self.codes = codes 

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
        # Return an object of this model
        return cls(codes)
