# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BasicDateField(object):

    """Implementation of the 'Basic Date Field' enum.

    Allows to filter by `created_at` or `updated_at`.

    Attributes:
        UPDATED_AT: The enum member of type str.
        CREATED_AT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    UPDATED_AT = 'updated_at'

    CREATED_AT = 'created_at'

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
