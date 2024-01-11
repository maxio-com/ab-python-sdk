# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ItemCategory(object):

    """Implementation of the 'Item Category' enum.

    One of the following: Business Software, Consumer Software, Digital
    Services, Physical Goods, Other

    Attributes:
        ENUM_BUSINESS SOFTWARE: TODO: type description here.
        ENUM_CONSUMER SOFTWARE: TODO: type description here.
        ENUM_DIGITAL SERVICES: TODO: type description here.
        ENUM_PHYSICAL GOODS: TODO: type description here.
        OTHER: TODO: type description here.

    """
    _all_values = ['Business Software', 'Consumer Software', 'Digital Services', 'Physical Goods', 'Other']
    ENUM_BUSINESS_SOFTWARE = 'Business Software'

    ENUM_CONSUMER_SOFTWARE = 'Consumer Software'

    ENUM_DIGITAL_SERVICES = 'Digital Services'

    ENUM_PHYSICAL_GOODS = 'Physical Goods'

    OTHER = 'Other'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
