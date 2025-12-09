# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SubscriptionDateField(object):

    """Implementation of the 'Subscription Date Field' enum.

    Attributes:
        CURRENT_PERIOD_ENDS_AT: The enum member of type str.
        CURRENT_PERIOD_STARTS_AT: The enum member of type str.
        CREATED_AT: The enum member of type str.
        ACTIVATED_AT: The enum member of type str.
        CANCELED_AT: The enum member of type str.
        EXPIRES_AT: The enum member of type str.
        TRIAL_STARTED_AT: The enum member of type str.
        TRIAL_ENDED_AT: The enum member of type str.
        UPDATED_AT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    CURRENT_PERIOD_ENDS_AT = 'current_period_ends_at'

    CURRENT_PERIOD_STARTS_AT = 'current_period_starts_at'

    CREATED_AT = 'created_at'

    ACTIVATED_AT = 'activated_at'

    CANCELED_AT = 'canceled_at'

    EXPIRES_AT = 'expires_at'

    TRIAL_STARTED_AT = 'trial_started_at'

    TRIAL_ENDED_AT = 'trial_ended_at'

    UPDATED_AT = 'updated_at'

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
