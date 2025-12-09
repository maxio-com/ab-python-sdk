# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TrialType(object):

    """Implementation of the 'Trial Type' enum.

    Indicates how a trial is handled when the trail period ends and there is
    no credit card on file. For `no_obligation`, the subscription transitions
    to a Trial Ended state. Maxio will not send any emails or statements. For
    `payment_expected`, the subscription transitions to a Past Due state.
    Maxio will send normal dunning emails and statements according to your
    other settings.

    Attributes:
        NO_OBLIGATION: The enum member of type str.
        PAYMENT_EXPECTED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['no_obligation', 'payment_expected']
    NO_OBLIGATION = 'no_obligation'

    PAYMENT_EXPECTED = 'payment_expected'

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
