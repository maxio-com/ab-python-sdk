"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SortBy(object):
    """Implementation of the 'sort_by' enum.

    Attributes:
        NAME: The enum member of type str.
        UPDATED_AT: The enum member of type str.
        KIND: The enum member of type str.
        VALUE_TYPE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    NAME = "name"

    UPDATED_AT = "updated_at"

    KIND = "kind"

    VALUE_TYPE = "value_type"

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
