"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class CollectionMethod1(object):
    """Implementation of the 'collection_method1' enum.

    Attributes:
        AUTOMATIC: The enum member of type str.
        REMITTANCE: The enum member of type str.
        PREPAID: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    AUTOMATIC = "automatic"

    REMITTANCE = "remittance"

    PREPAID = "prepaid"

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
