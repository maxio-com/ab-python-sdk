# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DebitNoteStatus(object):

    """Implementation of the 'Debit Note Status' enum.

    Current status of the debit note.

    Attributes:
        OPEN: TODO: type description here.
        APPLIED: TODO: type description here.
        BANISHED: TODO: type description here.
        PAID: TODO: type description here.

    """
    _all_values = ['open', 'applied', 'banished', 'paid']
    OPEN = 'open'

    APPLIED = 'applied'

    BANISHED = 'banished'

    PAID = 'paid'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   