# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceRole(object):

    """Implementation of the 'Invoice Role' enum.

    Attributes:
        UNSET: The enum member of type str.
        SIGNUP: The enum member of type str.
        RENEWAL: The enum member of type str.
        USAGE: The enum member of type str.
        REACTIVATION: The enum member of type str.
        PRORATION: The enum member of type str.
        MIGRATION: The enum member of type str.
        ADHOC: The enum member of type str.
        BACKPORT: The enum member of type str.
        BACKPORTBALANCERECONCILIATION: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['unset', 'signup', 'renewal', 'usage', 'reactivation', 'proration', 'migration', 'adhoc', 'backport', 'backport-balance-reconciliation']
    UNSET = 'unset'

    SIGNUP = 'signup'

    RENEWAL = 'renewal'

    USAGE = 'usage'

    REACTIVATION = 'reactivation'

    PRORATION = 'proration'

    MIGRATION = 'migration'

    ADHOC = 'adhoc'

    BACKPORT = 'backport'

    BACKPORTBALANCERECONCILIATION = 'backport-balance-reconciliation'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   
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
