# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PrepaidSubscriptionBalanceChanged(object):

    """Implementation of the 'Prepaid Subscription Balance Changed' model.

    TODO: type model description here.

    Attributes:
        reason (str): TODO: type description here.
        current_account_balance_in_cents (long|int): TODO: type description
            here.
        prepayment_account_balance_in_cents (long|int): TODO: type description
            here.
        current_usage_amount_in_cents (long|int): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason',
        "current_account_balance_in_cents": 'current_account_balance_in_cents',
        "prepayment_account_balance_in_cents": 'prepayment_account_balance_in_cents',
        "current_usage_amount_in_cents": 'current_usage_amount_in_cents'
    }

    def __init__(self,
                 reason=None,
                 current_account_balance_in_cents=None,
                 prepayment_account_balance_in_cents=None,
                 current_usage_amount_in_cents=None):
        """Constructor for the PrepaidSubscriptionBalanceChanged class"""

        # Initialize members of the class
        self.reason = reason 
        self.current_account_balance_in_cents = current_account_balance_in_cents 
        self.prepayment_account_balance_in_cents = prepayment_account_balance_in_cents 
        self.current_usage_amount_in_cents = current_usage_amount_in_cents 

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
        current_account_balance_in_cents = dictionary.get("current_account_balance_in_cents") if dictionary.get("current_account_balance_in_cents") else None
        prepayment_account_balance_in_cents = dictionary.get("prepayment_account_balance_in_cents") if dictionary.get("prepayment_account_balance_in_cents") else None
        current_usage_amount_in_cents = dictionary.get("current_usage_amount_in_cents") if dictionary.get("current_usage_amount_in_cents") else None
        # Return an object of this model
        return cls(reason,
                   current_account_balance_in_cents,
                   prepayment_account_balance_in_cents,
                   current_usage_amount_in_cents)

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
                and APIHelper.is_valid_type(value=dictionary.current_account_balance_in_cents, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.prepayment_account_balance_in_cents, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.current_usage_amount_in_cents, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('reason'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_account_balance_in_cents'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('prepayment_account_balance_in_cents'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_usage_amount_in_cents'), type_callable=lambda value: isinstance(value, int))
