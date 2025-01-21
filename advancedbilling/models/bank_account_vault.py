# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountVault(object):

    """Implementation of the 'Bank Account Vault' enum.

    The vault that stores the payment profile with the provided vault_token.
    Use `bogus` for testing.

    Attributes:
        AUTHORIZENET: The enum member of type str.
        BLUE_SNAP: The enum member of type str.
        BOGUS: The enum member of type str.
        FORTE: The enum member of type str.
        GOCARDLESS: The enum member of type str.
        MAXIO_PAYMENTS: The enum member of type str.
        MAXP: The enum member of type str.
        STRIPE_CONNECT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['authorizenet', 'blue_snap', 'bogus', 'forte', 'gocardless', 'maxio_payments', 'maxp', 'stripe_connect']
    AUTHORIZENET = 'authorizenet'

    BLUE_SNAP = 'blue_snap'

    BOGUS = 'bogus'

    FORTE = 'forte'

    GOCARDLESS = 'gocardless'

    MAXIO_PAYMENTS = 'maxio_payments'

    MAXP = 'maxp'

    STRIPE_CONNECT = 'stripe_connect'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   