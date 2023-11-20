# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.payment_profile import PaymentProfile


class PaymentProfileResponse(object):

    """Implementation of the 'Payment Profile Response' model.

    TODO: type model description here.

    Attributes:
        payment_profile (PaymentProfile): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_profile": 'payment_profile'
    }

    def __init__(self,
                 payment_profile=None):
        """Constructor for the PaymentProfileResponse class"""

        # Initialize members of the class
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
        payment_profile = PaymentProfile.from_dictionary(dictionary.get('payment_profile')) if dictionary.get('payment_profile') else None
        # Return an object of this model
        return cls(payment_profile)
