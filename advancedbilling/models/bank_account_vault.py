# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountVault(object):

    """Implementation of the 'Bank Account Vault' enum.

    The vault that stores the payment profile with the provided vault_token.

    Attributes:
        BOGUS: TODO: type description here.
        AUTHORIZENET: TODO: type description here.
        STRIPE_CONNECT: TODO: type description here.
        BRAINTREE_BLUE: TODO: type description here.
        GOCARDLESS: TODO: type description here.

    """
    _all_values = ['bogus', 'authorizenet', 'stripe_connect', 'braintree_blue', 'gocardless']
    BOGUS = 'bogus'

    AUTHORIZENET = 'authorizenet'

    STRIPE_CONNECT = 'stripe_connect'

    BRAINTREE_BLUE = 'braintree_blue'

    GOCARDLESS = 'gocardless'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   