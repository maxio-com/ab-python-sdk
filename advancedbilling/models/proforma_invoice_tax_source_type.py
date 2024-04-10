# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ProformaInvoiceTaxSourceType(object):

    """Implementation of the 'Proforma Invoice Tax Source Type' enum.

    TODO: type enum description here.

    Attributes:
        TAX: TODO: type description here.
        AVALARA: TODO: type description here.

    """
    _all_values = ['Tax', 'Avalara']
    TAX = 'Tax'

    AVALARA = 'Avalara'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   