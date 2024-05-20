# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceRole1(object):

    """Implementation of the 'Invoice Role1' enum.

    The role of the credit note (e.g. 'general')

    Attributes:
        UNSET: TODO: type description here.
        SIGNUP: TODO: type description here.
        RENEWAL: TODO: type description here.
        USAGE: TODO: type description here.
        REACTIVATION: TODO: type description here.
        PRORATION: TODO: type description here.
        MIGRATION: TODO: type description here.
        ADHOC: TODO: type description here.
        BACKPORT: TODO: type description here.
        BACKPORTBALANCERECONCILIATION: TODO: type description here.

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
   