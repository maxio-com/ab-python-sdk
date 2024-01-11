# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RestrictionType(object):

    """Implementation of the 'Restriction Type' enum.

    TODO: type enum description here.

    Attributes:
        COMPONENT: TODO: type description here.
        PRODUCT: TODO: type description here.

    """
    _all_values = ['Component', 'Product']
    COMPONENT = 'Component'

    PRODUCT = 'Product'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
