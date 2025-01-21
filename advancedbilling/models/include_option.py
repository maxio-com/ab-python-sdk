# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class IncludeOption(object):

    """Implementation of the 'Include Option' enum.

    Attributes:
        EXCLUDE: The enum member of type str.
        INCLUDE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['0', '1']
    EXCLUDE = '0'

    INCLUDE = '1'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   