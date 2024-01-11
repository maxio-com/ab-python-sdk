# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoicePaymentMethodType(object):

    """Implementation of the 'Invoice Payment Method Type' enum.

    The type of payment method used.

    Attributes:
        CREDIT_CARD: TODO: type description here.
        CHECK: TODO: type description here.
        CASH: TODO: type description here.
        MONEY_ORDER: TODO: type description here.
        ACH: TODO: type description here.
        OTHER: TODO: type description here.

    """
    _all_values = ['credit_card', 'check', 'cash', 'money_order', 'ach', 'other']
    CREDIT_CARD = 'credit_card'

    CHECK = 'check'

    CASH = 'cash'

    MONEY_ORDER = 'money_order'

    ACH = 'ach'

    OTHER = 'other'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
