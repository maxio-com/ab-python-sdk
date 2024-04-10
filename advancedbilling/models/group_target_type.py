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
        CUSTOMER: TODO: type description here.
        SUBSCRIPTION: TODO: type description here.
        SELF: TODO: type description here.
        PARENT: TODO: type description here.
        ELDEST: TODO: type description here.

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
   