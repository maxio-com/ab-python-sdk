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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the ReferralValidationResponse class"""

        # Initialize members of the class
        if referral_code is not APIHelper.SKIP:
            self.referral_code = referral_code 

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
        referral_code = ReferralCode.from_dictionary(dictionary.get('referral_code')) if 'referral_code' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(referral_code,
                   additional_properties)
