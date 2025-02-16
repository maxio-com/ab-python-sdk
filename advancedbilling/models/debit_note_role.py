# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DebitNoteRole(object):

    """Implementation of the 'Debit Note Role' enum.

    The role of the debit note.

    Attributes:
        CHARGEBACK: The enum member of type str.
        REFUND: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['chargeback', 'refund']
    CHARGEBACK = 'chargeback'

    REFUND = 'refund'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   