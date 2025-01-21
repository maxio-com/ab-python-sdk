# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CompoundingStrategy(object):

    """Implementation of the 'Compounding Strategy' enum.

    Applicable only to stackable coupons. For `compound`, Percentage-based
    discounts will be calculated against the remaining price, after prior
    discounts have been calculated. For `full-price`, Percentage-based
    discounts will always be calculated against the original item price,
    before other discounts are applied.

    Attributes:
        COMPOUND: The enum member of type str.
        FULLPRICE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['compound', 'full-price']
    COMPOUND = 'compound'

    FULLPRICE = 'full-price'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   