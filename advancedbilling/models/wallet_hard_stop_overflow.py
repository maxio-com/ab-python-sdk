"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class WalletHardStopOverflow(object):
    """Implementation of the 'Wallet Hard Stop Overflow' enum.

    Behavior at the hard-stop boundary. `discard` drains the wallet to zero and
    rejects the excess (the default). `allow_negative` deducts the full amount,
    letting the balance go negative. The excess past the wallet's grants is booked as
    an overdraft ledger row with `grant_id` set to `null`.

    Attributes:
        DISCARD: The enum member of type str.
        ALLOW_NEGATIVE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["discard", "allow_negative"]
    DISCARD = "discard"

    ALLOW_NEGATIVE = "allow_negative"

    @classmethod
    def validate(cls, value):
        """Validate value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values

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
