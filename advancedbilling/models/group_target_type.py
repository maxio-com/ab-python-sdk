# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GroupTargetType(object):

    """Implementation of the 'Group Target Type' enum.

    The type of object indicated by the id attribute.

    Attributes:
        CUSTOMER: The enum member of type str.
        SUBSCRIPTION: The enum member of type str.
        SELF: The enum member of type str.
        PARENT: The enum member of type str.
        ELDEST: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['customer', 'subscription', 'self', 'parent', 'eldest']
    CUSTOMER = 'customer'

    SUBSCRIPTION = 'subscription'

    ENUM_SELF = 'self'

    PARENT = 'parent'

    ELDEST = 'eldest'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   