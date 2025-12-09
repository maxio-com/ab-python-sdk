# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceEventPaymentMethod(object):

    """Implementation of the 'Invoice Event Payment Method' enum.

    Attributes:
        APPLE_PAY: The enum member of type str.
        BANK_ACCOUNT: The enum member of type str.
        CREDIT_CARD: The enum member of type str.
        EXTERNAL: The enum member of type str.
        PAYPAL_ACCOUNT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['apple_pay', 'bank_account', 'credit_card', 'external', 'paypal_account']
    APPLE_PAY = 'apple_pay'

    BANK_ACCOUNT = 'bank_account'

    CREDIT_CARD = 'credit_card'

    EXTERNAL = 'external'

    PAYPAL_ACCOUNT = 'paypal_account'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   
    @classmethod
    def from_value(cls, value, default=None):
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
