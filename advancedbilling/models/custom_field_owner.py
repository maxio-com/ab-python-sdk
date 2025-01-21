# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CustomFieldOwner(object):

    """Implementation of the 'Custom Field Owner' enum.

    Attributes:
        CUSTOMER: The enum member of type str.
        SUBSCRIPTION: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['Customer', 'Subscription']
    CUSTOMER = 'Customer'

    SUBSCRIPTION = 'Subscription'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   