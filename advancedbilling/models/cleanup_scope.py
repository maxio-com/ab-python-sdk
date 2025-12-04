# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CleanupScope(object):

    """Implementation of the 'Cleanup scope' enum.

    all: Will clear all products, customers, and related subscriptions from
    the site. customers: Will clear only customers and related subscriptions
    (leaving the products untouched) for the site. Revenue will also be reset
    to 0.

    Attributes:
        ALL: The enum member of type str.
        CUSTOMERS: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    ALL = 'all'

    CUSTOMERS = 'customers'

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
