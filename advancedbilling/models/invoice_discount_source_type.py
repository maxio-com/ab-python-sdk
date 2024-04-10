# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceDiscountSourceType(object):

    """Implementation of the 'Invoice Discount Source Type' enum.

    TODO: type enum description here.

    Attributes:
        COUPON: TODO: type description here.
        REFERRAL: TODO: type description here.
        ENUM_AD HOC COUPON: TODO: type description here.

    """
    _all_values = ['Coupon', 'Referral', 'Ad Hoc Coupon']
    COUPON = 'Coupon'

    REFERRAL = 'Referral'

    ENUM_AD_HOC_COUPON = 'Ad Hoc Coupon'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   