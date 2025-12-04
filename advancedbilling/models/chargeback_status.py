# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ChargebackStatus(object):

    """Implementation of the 'Chargeback Status' enum.

    The current chargeback status.

    Attributes:
        OPEN: The enum member of type str.
        LOST: The enum member of type str.
        WON: The enum member of type str.
        CLOSED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['open', 'lost', 'won', 'closed']
    OPEN = 'open'

    LOST = 'lost'

    WON = 'won'

    CLOSED = 'closed'

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
