# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SortingDirection(object):

    """Implementation of the 'Sorting direction' enum.

    Used for sorting results.

    Attributes:
        ASC: TODO: type description here.
        DESC: TODO: type description here.

    """
    _all_values = ['asc', 'desc']
    ASC = 'asc'

    DESC = 'desc'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
