# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RecurringScheme(object):

    """Implementation of the 'Recurring Scheme' enum.

    TODO: type enum description here.

    Attributes:
        DO_NOT_RECUR: TODO: type description here.
        RECUR_INDEFINITELY: TODO: type description here.
        RECUR_WITH_DURATION: TODO: type description here.

    """
    _all_values = ['do_not_recur', 'recur_indefinitely', 'recur_with_duration']
    DO_NOT_RECUR = 'do_not_recur'

    RECUR_INDEFINITELY = 'recur_indefinitely'

    RECUR_WITH_DURATION = 'recur_with_duration'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
