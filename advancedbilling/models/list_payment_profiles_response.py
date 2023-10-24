# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.list_payment_profile_item import ListPaymentProfileItem


class ListPaymentProfilesResponse(object):

    """Implementation of the 'List Payment Profiles Response' model.

    TODO: type model description here.

    Attributes:
        payment_profile (ListPaymentProfileItem): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_profile": 'payment_profile'
    }

    _optionals = [
        'payment_profile',
    ]

    def __init__(self,
                 payment_profile=APIHelper.SKIP):
        """Constructor for the ListPaymentProfilesResponse class"""

        # Initialize members of the class
        if payment_profile is not APIHelper.SKIP:
            self.payment_profile = payment_profile 

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
        payment_profile = ListPaymentProfileItem.from_dictionary(dictionary.get('payment_profile')) if 'payment_profile' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment_profile)
