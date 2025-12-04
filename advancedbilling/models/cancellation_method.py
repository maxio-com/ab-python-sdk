# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CancellationMethod(object):

    """Implementation of the 'Cancellation Method' enum.

    The process used to cancel the subscription, if the subscription has been
    canceled. It is nil if the subscription's state is not canceled.

    Attributes:
        MERCHANT_UI: The enum member of type str.
        MERCHANT_API: The enum member of type str.
        DUNNING: The enum member of type str.
        BILLING_PORTAL: The enum member of type str.
        UNKNOWN: The enum member of type str.
        IMPORTED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['merchant_ui', 'merchant_api', 'dunning', 'billing_portal', 'unknown', 'imported']
    MERCHANT_UI = 'merchant_ui'

    MERCHANT_API = 'merchant_api'

    DUNNING = 'dunning'

    BILLING_PORTAL = 'billing_portal'

    UNKNOWN = 'unknown'

    IMPORTED = 'imported'

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
