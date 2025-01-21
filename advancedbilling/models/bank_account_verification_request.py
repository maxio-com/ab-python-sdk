# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.bank_account_verification import BankAccountVerification


class BankAccountVerificationRequest(object):

    """Implementation of the 'Bank Account Verification Request' model.

    Attributes:
        bank_account_verification (BankAccountVerification): The model
            property of type BankAccountVerification.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_account_verification": 'bank_account_verification'
    }

    def __init__(self,
                 bank_account_verification=None,
                 additional_properties=None):
        """Constructor for the BankAccountVerificationRequest class"""

        # Initialize members of the class
        self.bank_account_verification = bank_account_verification 

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
        bank_account_verification = BankAccountVerification.from_dictionary(dictionary.get('bank_account_verification')) if dictionary.get('bank_account_verification') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(bank_account_verification,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'bank_account_verification={self.bank_account_verification!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'bank_account_verification={self.bank_account_verification!s}, '
                f'additional_properties={self.additional_properties!s})')
