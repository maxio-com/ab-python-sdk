# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CompoundingStrategy(object):

    """Implementation of the 'Compounding Strategy' enum.

    TODO: type enum description here.

    Attributes:
        COMPOUND: TODO: type description here.
        FULLPRICE: TODO: type description here.

    """
    _all_values = ['compound', 'full-price']
    COMPOUND = 'compound'

    FULLPRICE = 'full-price'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   