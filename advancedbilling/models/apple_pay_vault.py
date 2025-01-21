# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApplePayVault(object):

    """Implementation of the 'Apple Pay Vault' enum.

    The vault that stores the payment profile with the provided vault_token.

    Attributes:
        BRAINTREE_BLUE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['braintree_blue']
    BRAINTREE_BLUE = 'braintree_blue'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   