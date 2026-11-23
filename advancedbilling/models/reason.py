"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class Reason(object):
    """Implementation of the 'Reason' enum.

    Set whenever `status` isn't `active`. Accompanying `stopped`:
    `entitlement_missing` (an ordinary product or component change removed the
    entitlement), `wallet_archived` (the wallet was archived),
    `subscription_terminated` (the subscription reached a terminal state; funding
    resumes if the subscription returns to a granting state, for example on
    reactivation, without back-granting the periods it missed), `feature_removed`
    (the subscription no longer has this Feature), `wallet_behavior_disabled` (the
    Feature no longer has `wallet_behavior` configured), `superseded_by_replacement`
    (a later entitlement now funds this wallet instead), or `subscription_prepaid`
    (the subscription switched to prepaid, which cannot carry an active wallet).
    Accompanying `erroring`: `allowance_not_representable` (the entitlement's current
    allowance doesn't fit the wallet's amount encoding) or `balance_at_capacity`
    (granting it would push the balance past the maximum supported value).

    Attributes:
        ENTITLEMENT_MISSING: The enum member of type str.
        WALLET_ARCHIVED: The enum member of type str.
        SUBSCRIPTION_TERMINATED: The enum member of type str.
        FEATURE_REMOVED: The enum member of type str.
        WALLET_BEHAVIOR_DISABLED: The enum member of type str.
        SUPERSEDED_BY_REPLACEMENT: The enum member of type str.
        SUBSCRIPTION_PREPAID: The enum member of type str.
        ALLOWANCE_NOT_REPRESENTABLE: The enum member of type str.
        BALANCE_AT_CAPACITY: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    ENTITLEMENT_MISSING = "entitlement_missing"

    WALLET_ARCHIVED = "wallet_archived"

    SUBSCRIPTION_TERMINATED = "subscription_terminated"

    FEATURE_REMOVED = "feature_removed"

    WALLET_BEHAVIOR_DISABLED = "wallet_behavior_disabled"

    SUPERSEDED_BY_REPLACEMENT = "superseded_by_replacement"

    SUBSCRIPTION_PREPAID = "subscription_prepaid"

    ALLOWANCE_NOT_REPRESENTABLE = "allowance_not_representable"

    BALANCE_AT_CAPACITY = "balance_at_capacity"

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
