"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class UpgradeChargeCreditType(object):
    """Implementation of the 'Upgrade Charge Credit Type' enum.

    The type of credit to be created when upgrading/downgrading. Defaults to the
    component and then site setting if one is not provided. Values are:
    `full` - A charge is added for the full price of the component.
    `prorated` - A charge is added for the prorated price of the component change.
    `none` - No charge is added.

    Attributes:
        FULL: The enum member of type str.
        PRORATED: The enum member of type str.
        NONE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["full", "prorated", "none"]
    FULL = "full"

    PRORATED = "prorated"

    NONE = "none"

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
