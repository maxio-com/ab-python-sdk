# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PaymentType(object):

    """Implementation of the 'Payment Type' enum.

    TODO: type enum description here.

    Attributes:
        CREDIT_CARD: TODO: type description here.
        BANK_ACCOUNT: TODO: type description here.
        PAYPAL_ACCOUNT: TODO: type description here.
        APPLE_PAY: TODO: type description here.

    """
    _all_values = ['credit_card', 'bank_account', 'paypal_account', 'apple_pay']
    CREDIT_CARD = 'credit_card'

    BANK_ACCOUNT = 'bank_account'

    PAYPAL_ACCOUNT = 'paypal_account'

    APPLE_PAY = 'apple_pay'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   