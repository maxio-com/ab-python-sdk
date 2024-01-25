# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountType(object):

    """Implementation of the 'Bank Account Type' enum.

    Defaults to checking

    Attributes:
        CHECKING: TODO: type description here.
        SAVINGS: TODO: type description here.

    """
    _all_values = ['checking', 'savings']
    CHECKING = 'checking'

    SAVINGS = 'savings'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
