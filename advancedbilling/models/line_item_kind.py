# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LineItemKind(object):

    """Implementation of the 'Line Item Kind' enum.

    A handle for the line item kind

    Attributes:
        BASELINE: The enum member of type str.
        INITIAL: The enum member of type str.
        TRIAL: The enum member of type str.
        QUANTITY_BASED_COMPONENT: The enum member of type str.
        PREPAID_USAGE_COMPONENT: The enum member of type str.
        ON_OFF_COMPONENT: The enum member of type str.
        METERED_COMPONENT: The enum member of type str.
        EVENT_BASED_COMPONENT: The enum member of type str.
        COUPON: The enum member of type str.
        TAX: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    BASELINE = 'baseline'

    INITIAL = 'initial'

    TRIAL = 'trial'

    QUANTITY_BASED_COMPONENT = 'quantity_based_component'

    PREPAID_USAGE_COMPONENT = 'prepaid_usage_component'

    ON_OFF_COMPONENT = 'on_off_component'

    METERED_COMPONENT = 'metered_component'

    EVENT_BASED_COMPONENT = 'event_based_component'

    COUPON = 'coupon'

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
