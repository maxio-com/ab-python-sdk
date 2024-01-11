# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FirstChargeType(object):

    """Implementation of the 'First Charge Type' enum.

    TODO: type enum description here.

    Attributes:
        PRORATED: TODO: type description here.
        IMMEDIATE: TODO: type description here.
        DELAYED: TODO: type description here.

    """
    _all_values = ['prorated', 'immediate', 'delayed']
    PRORATED = 'prorated'

    IMMEDIATE = 'immediate'

    DELAYED = 'delayed'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
