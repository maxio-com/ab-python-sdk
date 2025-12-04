# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BillingManifestLineItemKind(object):

    """Implementation of the 'Billing Manifest Line Item Kind' enum.

    A handle for the billing manifest line item kind

    Attributes:
        BASELINE: The enum member of type str.
        INITIAL: The enum member of type str.
        TRIAL: The enum member of type str.
        COUPON: The enum member of type str.
        COMPONENT: The enum member of type str.
        TAX: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    BASELINE = 'baseline'

    INITIAL = 'initial'

    TRIAL = 'trial'

    COUPON = 'coupon'

    COMPONENT = 'component'

    TAX = 'tax'

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
