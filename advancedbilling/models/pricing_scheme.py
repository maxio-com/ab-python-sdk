# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PricingScheme(object):

    """Implementation of the 'Pricing Scheme' enum.

    The identifier for the pricing scheme. See [Product
    Components](https://help.chargify.com/products/product-components.html)
    for an overview of pricing schemes.

    Attributes:
        STAIRSTEP: The enum member of type str.
        VOLUME: The enum member of type str.
        PER_UNIT: The enum member of type str.
        TIERED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['stairstep', 'volume', 'per_unit', 'tiered']
    STAIRSTEP = 'stairstep'

    VOLUME = 'volume'

    PER_UNIT = 'per_unit'

    TIERED = 'tiered'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   
    @classmethod
    def from_value(cls, value, default=None):
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
