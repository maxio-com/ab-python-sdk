# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoicePaymentType(object):

    """Implementation of the 'Invoice Payment Type' enum.

    The type of payment to be applied to an Invoice. Defaults to external.

    Attributes:
        EXTERNAL: The enum member of type str.
        PREPAYMENT: The enum member of type str.
        SERVICE_CREDIT: The enum member of type str.
        PAYMENT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    EXTERNAL = 'external'

    PREPAYMENT = 'prepayment'

    SERVICE_CREDIT = 'service_credit'

    PAYMENT = 'payment'

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
