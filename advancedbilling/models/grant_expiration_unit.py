"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class GrantExpirationUnit(object):
    """Implementation of the 'Grant Expiration Unit' enum.

    How long a wallet grant funded by a `usage_limit` feature stays spendable. `day`
    and `month` need a `grant_expiration_interval`; `until_next_refill` takes none
    and expires the grant when the next refill lands. Omit both fields for a grant
    that never expires.

    Attributes:
        DAY: The enum member of type str.
        MONTH: The enum member of type str.
        UNTIL_NEXT_REFILL: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    DAY = "day"

    MONTH = "month"

    UNTIL_NEXT_REFILL = "until_next_refill"

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
