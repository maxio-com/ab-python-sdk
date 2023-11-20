# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentMethodBankAccountType(object):

    """Implementation of the 'Payment Method Bank Account Type' model.

    TODO: type model description here.

    Attributes:
        masked_account_number (str): TODO: type description here.
        masked_routing_number (str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "masked_account_number": 'masked_account_number',
        "masked_routing_number": 'masked_routing_number',
        "mtype": 'type'
    }

    _optionals = [
        'masked_account_number',
        'masked_routing_number',
        'mtype',
    ]

    def __init__(self,
                 masked_account_number=APIHelper.SKIP,
                 masked_routing_number=APIHelper.SKIP,
                 mtype='bank_account'):
        """Constructor for the PaymentMethodBankAccountType class"""

        # Initialize members of the class
        if masked_account_number is not APIHelper.SKIP:
            self.masked_account_number = masked_account_number 
        if masked_routing_number is not APIHelper.SKIP:
            self.masked_routing_number = masked_routing_number 
        self.mtype = mtype 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        masked_account_number = dictionary.get("masked_account_number") if dictionary.get("masked_account_number") else APIHelper.SKIP
        masked_routing_number = dictionary.get("masked_routing_number") if dictionary.get("masked_routing_number") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'bank_account'
        # Return an object of this model
        return cls(masked_account_number,
                   masked_routing_number,
                   mtype)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
