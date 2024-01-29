# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BankAccountVerification(object):

    """Implementation of the 'Bank Account Verification' model.

    TODO: type model description here.

    Attributes:
        deposit_1_in_cents (long|int): TODO: type description here.
        deposit_2_in_cents (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deposit_1_in_cents": 'deposit_1_in_cents',
        "deposit_2_in_cents": 'deposit_2_in_cents'
    }

    _optionals = [
        'deposit_1_in_cents',
        'deposit_2_in_cents',
    ]

    def __init__(self,
                 deposit_1_in_cents=APIHelper.SKIP,
                 deposit_2_in_cents=APIHelper.SKIP):
        """Constructor for the BankAccountVerification class"""

        # Initialize members of the class
        if deposit_1_in_cents is not APIHelper.SKIP:
            self.deposit_1_in_cents = deposit_1_in_cents 
        if deposit_2_in_cents is not APIHelper.SKIP:
            self.deposit_2_in_cents = deposit_2_in_cents 

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
        deposit_1_in_cents = dictionary.get("deposit_1_in_cents") if dictionary.get("deposit_1_in_cents") else APIHelper.SKIP
        deposit_2_in_cents = dictionary.get("deposit_2_in_cents") if dictionary.get("deposit_2_in_cents") else APIHelper.SKIP
        # Return an object of this model
        return cls(deposit_1_in_cents,
                   deposit_2_in_cents)
