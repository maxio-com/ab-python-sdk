# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CancellationMethod(object):

    """Implementation of the 'Cancellation Method' enum.

    The process used to cancel the subscription, if the subscription has been
    canceled. It is nil if the subscription's state is not canceled.

    Attributes:
        MERCHANT_UI: TODO: type description here.
        MERCHANT_API: TODO: type description here.
        DUNNING: TODO: type description here.
        BILLING_PORTAL: TODO: type description here.

    """
    _all_values = ['merchant_ui', 'merchant_api', 'dunning', 'billing_portal']
    MERCHANT_UI = 'merchant_ui'

    MERCHANT_API = 'merchant_api'

    DUNNING = 'dunning'

    BILLING_PORTAL = 'billing_portal'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
