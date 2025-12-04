# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SortingDirection(object):

    """Implementation of the 'Sorting direction' enum.

    Used for sorting results.

    Attributes:
        ASC: The enum member of type str.
        DESC: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    ASC = 'asc'

    DESC = 'desc'

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
