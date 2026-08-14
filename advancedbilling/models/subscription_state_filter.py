"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SubscriptionStateFilter(object):
    """Implementation of the 'Subscription State Filter' enum.

    Allowed values for filtering by the current state of the subscription.

    Attributes:
        ACTIVE: The enum member of type str.
        CANCELED: The enum member of type str.
        EXPIRED: The enum member of type str.
        EXPIRED_CARDS: The enum member of type str.
        ENUM_EXPIRED_CARDS_LIVE_SUBSCRIPTIONS: The enum member of type str.
        ENUM_EXPIRED_CARDS_ALL_SUBSCRIPTIONS: The enum member of type str.
        ON_HOLD: The enum member of type str.
        AWAITING_SIGNUP: The enum member of type str.
        AWAITING_SIGNUP_DATE: The enum member of type str.
        PAST_DUE: The enum member of type str.
        PENDING_CANCELLATION: The enum member of type str.
        PENDING_RENEWAL: The enum member of type str.
        PREPAID_DUNNING: The enum member of type str.
        SUSPENDED: The enum member of type str.
        TRIAL_ENDED: The enum member of type str.
        TRIALING: The enum member of type str.
        UNPAID: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    ACTIVE = "active"

    CANCELED = "canceled"

    EXPIRED = "expired"

    EXPIRED_CARDS = "expired_cards"

    ENUM_EXPIRED_CARDS_LIVE_SUBSCRIPTIONS = "expired_cards_(live_subscriptions)"

    ENUM_EXPIRED_CARDS_ALL_SUBSCRIPTIONS = "expired_cards_(all_subscriptions)"

    ON_HOLD = "on_hold"

    AWAITING_SIGNUP = "awaiting_signup"

    AWAITING_SIGNUP_DATE = "awaiting_signup_date"

    PAST_DUE = "past_due"

    PENDING_CANCELLATION = "pending_cancellation"

    PENDING_RENEWAL = "pending_renewal"

    PREPAID_DUNNING = "prepaid_dunning"

    SUSPENDED = "suspended"

    TRIAL_ENDED = "trial_ended"

    TRIALING = "trialing"

    UNPAID = "unpaid"

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
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
