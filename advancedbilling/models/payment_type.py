"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class PaymentType(object):
    """Implementation of the 'Payment Type' enum.

    Attributes:
        CREDIT_CARD: The enum member of type str.
        BANK_ACCOUNT: The enum member of type str.
        PAYPAL_ACCOUNT: The enum member of type str.
        APPLE_PAY: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["credit_card", "bank_account", "paypal_account",
        "apple_pay"]
    CREDIT_CARD = "credit_card"

    BANK_ACCOUNT = "bank_account"

    PAYPAL_ACCOUNT = "paypal_account"

    APPLE_PAY = "apple_pay"

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
