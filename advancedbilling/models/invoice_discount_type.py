# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceDiscountType(object):

    """Implementation of the 'Invoice Discount Type' enum.

    Attributes:
        PERCENTAGE: The enum member of type str.
        FLAT_AMOUNT: The enum member of type str.
        ROLLOVER: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['percentage', 'flat_amount', 'rollover']
    PERCENTAGE = 'percentage'

    FLAT_AMOUNT = 'flat_amount'

    ROLLOVER = 'rollover'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   