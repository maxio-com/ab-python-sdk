# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreditType(object):

    """Implementation of the 'Credit Type' enum.

    The type of credit to be created when upgrading/downgrading. Defaults to
    the component and then site setting if one is not provided.
    Available values: `full`, `prorated`, `none`.

    Attributes:
        FULL: TODO: type description here.
        PRORATED: TODO: type description here.
        NONE: TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['full', 'prorated', 'none']
    FULL = 'full'

    PRORATED = 'prorated'

    NONE = 'none'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   