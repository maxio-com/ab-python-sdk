# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PrepaidSubscriptionBalanceChanged(object):

    """Implementation of the 'Prepaid Subscription Balance Changed' model.

    Attributes:
        reason (str): The model property of type str.
        current_account_balance_in_cents (int): The model property of type int.
        prepayment_account_balance_in_cents (int): The model property of type
            int.
        current_usage_amount_in_cents (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 current_usage_amount_in_cents=None,
                 additional_properties=None):
        """Constructor for the PrepaidSubscriptionBalanceChanged class"""

        # Initialize members of the class
        self.reason = reason 
        self.current_account_balance_in_cents = current_account_balance_in_cents 
        self.prepayment_account_balance_in_cents = prepayment_account_balance_in_cents 
        self.current_usage_amount_in_cents = current_usage_amount_in_cents 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        current_account_balance_in_cents = dictionary.get("current_account_balance_in_cents") if dictionary.get("current_account_balance_in_cents") else None
        prepayment_account_balance_in_cents = dictionary.get("prepayment_account_balance_in_cents") if dictionary.get("prepayment_account_balance_in_cents") else None
        current_usage_amount_in_cents = dictionary.get("current_usage_amount_in_cents") if dictionary.get("current_usage_amount_in_cents") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(reason,
                   current_account_balance_in_cents,
                   prepayment_account_balance_in_cents,
                   current_usage_amount_in_cents,
                   additional_properties)

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
                and APIHelper.is_valid_type(value=dictionary.current_account_balance_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.prepayment_account_balance_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.current_usage_amount_in_cents,
                                            type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('reason'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_account_balance_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('prepayment_account_balance_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_usage_amount_in_cents'),
                                        type_callable=lambda value: isinstance(value, int))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'reason={self.reason!r}, '
                f'current_account_balance_in_cents={self.current_account_balance_in_cents!r}, '
                f'prepayment_account_balance_in_cents={self.prepayment_account_balance_in_cents!r}, '
                f'current_usage_amount_in_cents={self.current_usage_amount_in_cents!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'reason={self.reason!s}, '
                f'current_account_balance_in_cents={self.current_account_balance_in_cents!s}, '
                f'prepayment_account_balance_in_cents={self.prepayment_account_balance_in_cents!s}, '
                f'current_usage_amount_in_cents={self.current_usage_amount_in_cents!s}, '
                f'additional_properties={self.additional_properties!s})')
