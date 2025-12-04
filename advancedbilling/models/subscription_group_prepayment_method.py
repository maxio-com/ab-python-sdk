# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SubscriptionGroupPrepaymentMethod(object):

    """Implementation of the 'Subscription Group Prepayment Method' enum.

    Attributes:
        CHECK: The enum member of type str.
        CASH: The enum member of type str.
        MONEY_ORDER: The enum member of type str.
        ACH: The enum member of type str.
        PAYPAL_ACCOUNT: The enum member of type str.
        OTHER: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    CHECK = 'check'

    CASH = 'cash'

    MONEY_ORDER = 'money_order'

    ACH = 'ach'

    PAYPAL_ACCOUNT = 'paypal_account'

    OTHER = 'other'

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
