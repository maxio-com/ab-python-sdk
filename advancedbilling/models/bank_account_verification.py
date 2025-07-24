# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BankAccountVerification(object):

    """Implementation of the 'Bank Account Verification' model.

    Attributes:
        deposit_1_in_cents (int): The model property of type int.
        deposit_2_in_cents (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 deposit_2_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the BankAccountVerification class"""

        # Initialize members of the class
        if deposit_1_in_cents is not APIHelper.SKIP:
            self.deposit_1_in_cents = deposit_1_in_cents 
        if deposit_2_in_cents is not APIHelper.SKIP:
            self.deposit_2_in_cents = deposit_2_in_cents 

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
        deposit_1_in_cents = dictionary.get("deposit_1_in_cents") if dictionary.get("deposit_1_in_cents") else APIHelper.SKIP
        deposit_2_in_cents = dictionary.get("deposit_2_in_cents") if dictionary.get("deposit_2_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(deposit_1_in_cents,
                   deposit_2_in_cents,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'deposit_1_in_cents={(self.deposit_1_in_cents if hasattr(self, "deposit_1_in_cents") else None)!r}, '
                f'deposit_2_in_cents={(self.deposit_2_in_cents if hasattr(self, "deposit_2_in_cents") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'deposit_1_in_cents={(self.deposit_1_in_cents if hasattr(self, "deposit_1_in_cents") else None)!s}, '
                f'deposit_2_in_cents={(self.deposit_2_in_cents if hasattr(self, "deposit_2_in_cents") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
