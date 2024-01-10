# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class IncludeOption(object):

    """Implementation of the 'Include Option' enum.

    TODO: type enum description here.

    Attributes:
        EXCLUDE: TODO: type description here.
        INCLUDE: TODO: type description here.

    """
    _all_values = ['0', '1']
    EXCLUDE = '0'

    INCLUDE = '1'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
