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
        OPEN: The enum member of type str.
        APPLIED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
   