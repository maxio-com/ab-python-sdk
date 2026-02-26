"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class MetafieldInput(object):
    """Implementation of the 'Metafield Input' enum.

    Indicates the type of metafield. A text metafield allows any string value.
    Dropdown and radio metafields have a set of values that can be selected.
    Defaults to 'text'.

    Attributes:
        BALANCE_TRACKER: The enum member of type str.
        TEXT: The enum member of type str.
        RADIO: The enum member of type str.
        DROPDOWN: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["balance_tracker", "text", "radio", "dropdown"]
    BALANCE_TRACKER = "balance_tracker"

    TEXT = "text"

    RADIO = "radio"

    DROPDOWN = "dropdown"

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
