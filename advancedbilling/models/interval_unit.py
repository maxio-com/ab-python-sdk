# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class IntervalUnit(object):

    """Implementation of the 'Interval Unit' enum.

    TODO: type enum description here.

    Attributes:
        DAY: TODO: type description here.
        MONTH: TODO: type description here.

    """
    _all_values = ['day', 'month']
    DAY = 'day'

    MONTH = 'month'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
