# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SnapDay(object):

    """Implementation of the 'SnapDay' enum.

    Use for subscriptions with product eligible for calendar billing only.
    Value can be 1-28 or 'end'.

    Attributes:
        END: TODO: type description here.

    """
    _all_values = ['end']
    END = 'end'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
