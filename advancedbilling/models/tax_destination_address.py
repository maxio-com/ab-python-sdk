# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TaxDestinationAddress(object):

    """Implementation of the 'Tax Destination Address' enum.

    Attributes:
        SHIPPING_THEN_BILLING: The enum member of type str.
        BILLING_THEN_SHIPPING: The enum member of type str.
        SHIPPING_ONLY: The enum member of type str.
        BILLING_ONLY: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    SHIPPING_THEN_BILLING = 'shipping_then_billing'

    BILLING_THEN_SHIPPING = 'billing_then_shipping'

    SHIPPING_ONLY = 'shipping_only'

    BILLING_ONLY = 'billing_only'

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
