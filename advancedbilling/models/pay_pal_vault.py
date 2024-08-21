# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PayPalVault(object):

    """Implementation of the 'PayPal Vault' enum.

    The vault that stores the payment profile with the provided vault_token.

    Attributes:
        BRAINTREE_BLUE: TODO: type description here.
        PAYPAL: TODO: type description here.
        MODUSLINK: TODO: type description here.
        PAYPAL_COMPLETE: TODO: type description here.

    """
    _all_values = ['braintree_blue', 'paypal', 'moduslink', 'paypal_complete']
    BRAINTREE_BLUE = 'braintree_blue'

    PAYPAL = 'paypal'

    MODUSLINK = 'moduslink'

    PAYPAL_COMPLETE = 'paypal_complete'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   