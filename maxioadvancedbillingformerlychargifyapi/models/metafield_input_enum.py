# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class MetafieldInputEnum(object):

    """Implementation of the 'Metafield Input' enum.

    Indicates how data should be added to the metafield. For example, a text
    type is just a string, so a given metafield of this type can have any
    value attached. On the other hand, dropdown and radio have a set of
    allowed values that can be input, and appear differently on a Public
    Signup Page.

    Attributes:
        TEXT: TODO: type description here.
        RADIO: TODO: type description here.
        DROPDOWN: TODO: type description here.

    """
    _all_values = ['text', 'radio', 'dropdown']
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
