# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreditAccountBalanceChanged(object):

    """Implementation of the 'Credit Account Balance Changed' model.

    TODO: type model description here.

    Attributes:
        reason (str): TODO: type description here.
        service_credit_account_balance_in_cents (int): TODO: type description
            here.
        service_credit_balance_change_in_cents (int): TODO: type description
            here.
        currency_code (str): TODO: type description here.
        at_time (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason',
        "service_credit_account_balance_in_cents": 'service_credit_account_balance_in_cents',
        "service_credit_balance_change_in_cents": 'service_credit_balance_change_in_cents',
        "currency_code": 'currency_code',
        "at_time": 'at_time'
    }

    def __init__(self,
                 reason=None,
                 service_credit_account_balance_in_cents=None,
                 service_credit_balance_change_in_cents=None,
                 currency_code=None,
                 at_time=None):
        """Constructor for the CreditAccountBalanceChanged class"""

        # Initialize members of the class
        self.reason = reason 
        self.service_credit_account_balance_in_cents = service_credit_account_balance_in_cents 
        self.service_credit_balance_change_in_cents = service_credit_balance_change_in_cents 
        self.currency_code = currency_code 
        self.at_time = at_time 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        service_credit_account_balance_in_cents = dictionary.get("service_credit_account_balance_in_cents") if dictionary.get("service_credit_account_balance_in_cents") else None
        service_credit_balance_change_in_cents = dictionary.get("service_credit_balance_change_in_cents") if dictionary.get("service_credit_balance_change_in_cents") else None
        currency_code = dictionary.get("currency_code") if dictionary.get("currency_code") else None
        at_time = dictionary.get("at_time") if dictionary.get("at_time") else None
        # Return an object of this model
        return cls(reason,
                   service_credit_account_balance_in_cents,
                   service_credit_balance_change_in_cents,
                   currency_code,
                   at_time)

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
            return APIHelper.is_valid_type(value=dictionary.reason, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.service_credit_account_balance_in_cents, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.service_credit_balance_change_in_cents, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.currency_code, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.at_time, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('reason'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('service_credit_account_balance_in_cents'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('service_credit_balance_change_in_cents'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('currency_code'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('at_time'), type_callable=lambda value: isinstance(value, str))
