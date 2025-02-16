# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreditAccountBalanceChanged(object):

    """Implementation of the 'Credit Account Balance Changed' model.

    Attributes:
        reason (str): The model property of type str.
        service_credit_account_balance_in_cents (int): The model property of
            type int.
        service_credit_balance_change_in_cents (int): The model property of
            type int.
        currency_code (str): The model property of type str.
        at_time (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 at_time=None,
                 additional_properties=None):
        """Constructor for the CreditAccountBalanceChanged class"""

        # Initialize members of the class
        self.reason = reason 
        self.service_credit_account_balance_in_cents = service_credit_account_balance_in_cents 
        self.service_credit_balance_change_in_cents = service_credit_balance_change_in_cents 
        self.currency_code = currency_code 
        self.at_time = APIHelper.apply_datetime_converter(at_time, APIHelper.RFC3339DateTime) if at_time else None 

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
        service_credit_account_balance_in_cents = dictionary.get("service_credit_account_balance_in_cents") if dictionary.get("service_credit_account_balance_in_cents") else None
        service_credit_balance_change_in_cents = dictionary.get("service_credit_balance_change_in_cents") if dictionary.get("service_credit_balance_change_in_cents") else None
        currency_code = dictionary.get("currency_code") if dictionary.get("currency_code") else None
        at_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("at_time")).datetime if dictionary.get("at_time") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(reason,
                   service_credit_account_balance_in_cents,
                   service_credit_balance_change_in_cents,
                   currency_code,
                   at_time,
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
                and APIHelper.is_valid_type(value=dictionary.service_credit_account_balance_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.service_credit_balance_change_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.currency_code,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.at_time,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('reason'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('service_credit_account_balance_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('service_credit_balance_change_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('currency_code'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('at_time'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'reason={self.reason!r}, '
                f'service_credit_account_balance_in_cents={self.service_credit_account_balance_in_cents!r}, '
                f'service_credit_balance_change_in_cents={self.service_credit_balance_change_in_cents!r}, '
                f'currency_code={self.currency_code!r}, '
                f'at_time={self.at_time!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'reason={self.reason!s}, '
                f'service_credit_account_balance_in_cents={self.service_credit_account_balance_in_cents!s}, '
                f'service_credit_balance_change_in_cents={self.service_credit_balance_change_in_cents!s}, '
                f'currency_code={self.currency_code!s}, '
                f'at_time={self.at_time!s}, '
                f'additional_properties={self.additional_properties!s})')
