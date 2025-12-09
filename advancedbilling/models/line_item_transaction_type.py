# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LineItemTransactionType(object):

    """Implementation of the 'Line Item Transaction Type' enum.

    A handle for the line item transaction type

    Attributes:
        CHARGE: The enum member of type str.
        CREDIT: The enum member of type str.
        ADJUSTMENT: The enum member of type str.
        PAYMENT: The enum member of type str.
        REFUND: The enum member of type str.
        INFO_TRANSACTION: The enum member of type str.
        PAYMENT_AUTHORIZATION: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    CHARGE = 'charge'

    CREDIT = 'credit'

    ADJUSTMENT = 'adjustment'

    PAYMENT = 'payment'

    REFUND = 'refund'

    INFO_TRANSACTION = 'info_transaction'

    PAYMENT_AUTHORIZATION = 'payment_authorization'

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
