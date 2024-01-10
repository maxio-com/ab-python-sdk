# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DiscountType(object):

    """Implementation of the 'Discount Type' enum.

    TODO: type enum description here.

    Attributes:
        AMOUNT: TODO: type description here.
        PERCENT: TODO: type description here.

    """
    _all_values = ['amount', 'percent']
    AMOUNT = 'amount'

    PERCENT = 'percent'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
