# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AccountBalance(object):

    """Implementation of the 'Account Balance' model.

    TODO: type model description here.

    Attributes:
        balance_in_cents (long|int): The balance in cents.
        automatic_balance_in_cents (long|int): The automatic balance in cents.
        remittance_balance_in_cents (long|int): The remittance balance in
            cents.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "balance_in_cents": 'balance_in_cents',
        "automatic_balance_in_cents": 'automatic_balance_in_cents',
        "remittance_balance_in_cents": 'remittance_balance_in_cents'
    }

    _optionals = [
        'balance_in_cents',
        'automatic_balance_in_cents',
        'remittance_balance_in_cents',
    ]

    _nullables = [
        'automatic_balance_in_cents',
        'remittance_balance_in_cents',
    ]

    def __init__(self,
                 balance_in_cents=APIHelper.SKIP,
                 automatic_balance_in_cents=APIHelper.SKIP,
                 remittance_balance_in_cents=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the AccountBalance class"""

        # Initialize members of the class
        if balance_in_cents is not APIHelper.SKIP:
            self.balance_in_cents = balance_in_cents 
        if automatic_balance_in_cents is not APIHelper.SKIP:
            self.automatic_balance_in_cents = automatic_balance_in_cents 
        if remittance_balance_in_cents is not APIHelper.SKIP:
            self.remittance_balance_in_cents = remittance_balance_in_cents 

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
        balance_in_cents = dictionary.get("balance_in_cents") if dictionary.get("balance_in_cents") else APIHelper.SKIP
        automatic_balance_in_cents = dictionary.get("automatic_balance_in_cents") if "automatic_balance_in_cents" in dictionary.keys() else APIHelper.SKIP
        remittance_balance_in_cents = dictionary.get("remittance_balance_in_cents") if "remittance_balance_in_cents" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(balance_in_cents,
                   automatic_balance_in_cents,
                   remittance_balance_in_cents,
                   dictionary)
