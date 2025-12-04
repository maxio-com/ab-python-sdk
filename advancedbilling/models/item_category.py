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
        ENUM_BUSINESS SOFTWARE: The enum member of type str.
        ENUM_CONSUMER SOFTWARE: The enum member of type str.
        ENUM_DIGITAL SERVICES: The enum member of type str.
        ENUM_PHYSICAL GOODS: The enum member of type str.
        OTHER: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    ENUM_BUSINESS_SOFTWARE = 'Business Software'

    ENUM_CONSUMER_SOFTWARE = 'Consumer Software'

    ENUM_DIGITAL_SERVICES = 'Digital Services'

    ENUM_PHYSICAL_GOODS = 'Physical Goods'

    OTHER = 'Other'

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
