"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class QScope(object):
    """Implementation of the 'q_scope' enum.

    Attributes:
        FULL_NAME: The enum member of type str.
        FIRST_NAME: The enum member of type str.
        LAST_NAME: The enum member of type str.
        ORGANIZATION: The enum member of type str.
        CUSTOMER_REFERENCE: The enum member of type str.
        SUBSCRIPTION_REFERENCE: The enum member of type str.
        LAST_FOUR: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    FULL_NAME = "full_name"

    FIRST_NAME = "first_name"

    LAST_NAME = "last_name"

    ORGANIZATION = "organization"

    CUSTOMER_REFERENCE = "customer_reference"

    SUBSCRIPTION_REFERENCE = "subscription_reference"

    LAST_FOUR = "last_four"

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
