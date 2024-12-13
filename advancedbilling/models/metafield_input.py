# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class MetafieldInput(object):

    """Implementation of the 'Metafield Input' enum.

    Indicates how data should be added to the metafield. For example, a text
    type is just a string, so a given metafield of this type can have any
    value attached. On the other hand, dropdown and radio have a set of
    allowed values that can be input, and appear differently on a Public
    Signup Page. Defaults to 'text'

    Attributes:
        BALANCE_TRACKER: TODO: type description here.
        TEXT: TODO: type description here.
        RADIO: TODO: type description here.
        DROPDOWN: TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['balance_tracker', 'text', 'radio', 'dropdown']
    BALANCE_TRACKER = 'balance_tracker'

    TEXT = 'text'

    RADIO = 'radio'

    DROPDOWN = 'dropdown'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   