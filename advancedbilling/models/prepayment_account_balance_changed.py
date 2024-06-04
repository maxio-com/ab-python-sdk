# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PrepaymentAccountBalanceChanged(object):

    """Implementation of the 'Prepayment Account Balance Changed' model.

    TODO: type model description here.

    Attributes:
        reason (str): TODO: type description here.
        prepayment_account_balance_in_cents (long|int): TODO: type description
            here.
        prepayment_balance_change_in_cents (long|int): TODO: type description
            here.
        currency_code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason',
        "prepayment_account_balance_in_cents": 'prepayment_account_balance_in_cents',
        "prepayment_balance_change_in_cents": 'prepayment_balance_change_in_cents',
        "currency_code": 'currency_code'
    }

    def __init__(self,
                 reason=None,
                 prepayment_account_balance_in_cents=None,
                 prepayment_balance_change_in_cents=None,
                 currency_code=None,
                 additional_properties={}):
        """Constructor for the PrepaymentAccountBalanceChanged class"""

        # Initialize members of the class
        self.reason = reason 
        self.prepayment_account_balance_in_cents = prepayment_account_balance_in_cents 
        self.prepayment_balance_change_in_cents = prepayment_balance_change_in_cents 
        self.currency_code = currency_code 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        prepayment_account_balance_in_cents = dictionary.get("prepayment_account_balance_in_cents") if dictionary.get("prepayment_account_balance_in_cents") else None
        prepayment_balance_change_in_cents = dictionary.get("prepayment_balance_change_in_cents") if dictionary.get("prepayment_balance_change_in_cents") else None
        currency_code = dictionary.get("currency_code") if dictionary.get("currency_code") else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(reason,
                   prepayment_account_balance_in_cents,
                   prepayment_balance_change_in_cents,
                   currency_code,
                   dictionary)

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
            return APIHelper.is_valid_type(value=dictionary.reason,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.prepayment_account_balance_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.prepayment_balance_change_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.currency_code,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('reason'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('prepayment_account_balance_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('prepayment_balance_change_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('currency_code'),
                                        type_callable=lambda value: isinstance(value, str))
