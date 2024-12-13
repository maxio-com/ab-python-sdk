# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CouponSubcodesResponse(object):

    """Implementation of the 'Coupon Subcodes Response' model.

    TODO: type model description here.

    Attributes:
        created_codes (List[str]): TODO: type description here.
        duplicate_codes (List[str]): TODO: type description here.
        invalid_codes (List[str]): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_codes": 'created_codes',
        "duplicate_codes": 'duplicate_codes',
        "invalid_codes": 'invalid_codes'
    }

    _optionals = [
        'created_codes',
        'duplicate_codes',
        'invalid_codes',
    ]

    def __init__(self,
                 created_codes=APIHelper.SKIP,
                 duplicate_codes=APIHelper.SKIP,
                 invalid_codes=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CouponSubcodesResponse class"""

        # Initialize members of the class
        if created_codes is not APIHelper.SKIP:
            self.created_codes = created_codes 
        if duplicate_codes is not APIHelper.SKIP:
            self.duplicate_codes = duplicate_codes 
        if invalid_codes is not APIHelper.SKIP:
            self.invalid_codes = invalid_codes 

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
        created_codes = dictionary.get("created_codes") if dictionary.get("created_codes") else APIHelper.SKIP
        duplicate_codes = dictionary.get("duplicate_codes") if dictionary.get("duplicate_codes") else APIHelper.SKIP
        invalid_codes = dictionary.get("invalid_codes") if dictionary.get("invalid_codes") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(created_codes,
                   duplicate_codes,
                   invalid_codes,
                   additional_properties)
