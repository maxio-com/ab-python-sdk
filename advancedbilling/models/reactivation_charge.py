# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ReactivationCharge(object):

    """Implementation of the 'Reactivation Charge' enum.

    You may choose how to handle the reactivation charge for that
    subscription: 1) `prorated` A prorated charge for the product price will
    be attempted for to complete the period 2) `immediate` A full-price charge
    for the product price will be attempted immediately 3) `delayed` A
    full-price charge for the product price will be attempted at the next
    renewal

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
   