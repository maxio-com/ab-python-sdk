# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PricePointType(object):

    """Implementation of the 'Price Point Type' enum.

    Price point type. We expose the following types:
    1. **default**: a price point that is marked as a default price for a
    certain product.
    2. **custom**: a custom price point.
    3. **catalog**: a price point that is **not** marked as a default price
    for a certain product and is **not** a custom one.

    Attributes:
        CATALOG: TODO: type description here.
        DEFAULT: TODO: type description here.
        CUSTOM: TODO: type description here.

    """
    _all_values = ['catalog', 'default', 'custom']
    CATALOG = 'catalog'

    DEFAULT = 'default'

    CUSTOM = 'custom'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   