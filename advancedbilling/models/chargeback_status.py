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
        OPEN: TODO: type description here.
        LOST: TODO: type description here.
        WON: TODO: type description here.
        CLOSED: TODO: type description here.
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
   