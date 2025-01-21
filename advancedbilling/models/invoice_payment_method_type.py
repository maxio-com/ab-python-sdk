# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoicePaymentMethodType(object):

    """Implementation of the 'Invoice Payment Method Type' enum.

    The type of payment method used. Defaults to other.

    Attributes:
        CREDIT_CARD: The enum member of type str.
        CHECK: The enum member of type str.
        CASH: The enum member of type str.
        MONEY_ORDER: The enum member of type str.
        ACH: The enum member of type str.
        OTHER: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
   