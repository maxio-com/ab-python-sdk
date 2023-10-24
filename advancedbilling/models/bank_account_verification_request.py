# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.bank_account_verification import BankAccountVerification


class BankAccountVerificationRequest(object):

    """Implementation of the 'Bank Account Verification Request' model.

    TODO: type model description here.

    Attributes:
        bank_account_verification (BankAccountVerification): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_account_verification": 'bank_account_verification'
    }

    def __init__(self,
                 bank_account_verification=None):
        """Constructor for the BankAccountVerificationRequest class"""

        # Initialize members of the class
        self.bank_account_verification = bank_account_verification 

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
        bank_account_verification = BankAccountVerification.from_dictionary(dictionary.get('bank_account_verification')) if dictionary.get('bank_account_verification') else None
        # Return an object of this model
        return cls(bank_account_verification)
