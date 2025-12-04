# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ReactivationCharge(object):

    """Implementation of the 'Reactivation Charge' enum.

    You may choose how to handle the reactivation charge for that
    subscription: 1) `prorated` A prorated charge for the product price will
    be attempted for to complete the period 2) `immediate` A full-price charge
    for the product price will be attempted immediately 3) `delayed` A
    full-price charge for the product price will be attempted at the next
    renewal

    Attributes:
        PRORATED: The enum member of type str.
        IMMEDIATE: The enum member of type str.
        DELAYED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['prorated', 'immediate', 'delayed']
    PRORATED = 'prorated'

    IMMEDIATE = 'immediate'

    DELAYED = 'delayed'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   
    @classmethod
    def from_value(cls, value, default=None):
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
