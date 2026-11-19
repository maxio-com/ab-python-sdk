"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class FeatureKind(object):
    """Implementation of the 'Feature Kind' enum.

    The behavior of a feature:
    - `access_right`: a boolean entitlement. A subscriber either has access or does
    not.
    - `usage_limit`: a quantified allowance measured over a recurring period (for
    example, "10,000 API calls per month").
    - `service_right`: a free-form value (text, boolean, or number) that isn't a
    simple access flag or a metered limit.

    Attributes:
        ACCESS_RIGHT: The enum member of type str.
        USAGE_LIMIT: The enum member of type str.
        SERVICE_RIGHT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["access_right", "usage_limit", "service_right"]
    ACCESS_RIGHT = "access_right"

    USAGE_LIMIT = "usage_limit"

    SERVICE_RIGHT = "service_right"

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
