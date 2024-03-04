# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.referral_code import ReferralCode


class ReferralValidationResponse(object):

    """Implementation of the 'Referral Validation Response' model.

    TODO: type model description here.

    Attributes:
        referral_code (ReferralCode): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "referral_code": 'referral_code'
    }

    _optionals = [
        'referral_code',
    ]

    def __init__(self,
                 referral_code=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ReferralValidationResponse class"""

        # Initialize members of the class
        if referral_code is not APIHelper.SKIP:
            self.referral_code = referral_code 

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
        referral_code = ReferralCode.from_dictionary(dictionary.get('referral_code')) if 'referral_code' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(referral_code,
                   dictionary)
