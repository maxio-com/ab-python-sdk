# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreditNoteStatus(object):

    """Implementation of the 'Credit Note Status' enum.

    Current status of the credit note.

    Attributes:
        OPEN: TODO: type description here.
        APPLIED: TODO: type description here.

    """
    _all_values = ['open', 'applied']
    OPEN = 'open'

    APPLIED = 'applied'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   