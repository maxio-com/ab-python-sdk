# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountHolderType(object):

    """Implementation of the 'Bank Account Holder Type' enum.

    Defaults to personal

    Attributes:
        PERSONAL: TODO: type description here.
        BUSINESS: TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['personal', 'business']
    PERSONAL = 'personal'

    BUSINESS = 'business'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   