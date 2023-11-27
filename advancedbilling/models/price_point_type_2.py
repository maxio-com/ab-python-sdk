# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PricePointType2(object):

    """Implementation of the 'Price Point Type2' enum.

    The type of price point

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
