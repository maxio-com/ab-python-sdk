"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class FeatureOwnerPricePointType(object):
    """Implementation of the 'Feature Owner Price Point Type' enum.

    Identifies which kind of price point a feature catalog item override applies to:
    `ProductPricePoint` for a product price point, `PricePoint` for a component price
    point. Only relevant when `price_point_id` is set.

    Attributes:
        PRODUCTPRICEPOINT: The enum member of type str.
        PRICEPOINT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    PRODUCTPRICEPOINT = "ProductPricePoint"

    PRICEPOINT = "PricePoint"

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
