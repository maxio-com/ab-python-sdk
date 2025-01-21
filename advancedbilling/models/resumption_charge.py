# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ResumptionCharge(object):

    """Implementation of the 'Resumption Charge' enum.

    (For calendar billing subscriptions only) The way that the resumed
    subscription's charge should be handled

    Attributes:
        PRORATED: The enum member of type str.
        IMMEDIATE: The enum member of type str.
        DELAYED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['prorated', 'immediate', 'delayed']
    PRORATED = 'prorated'

    IMMEDIATE = 'immediate'

    DELAYED = 'delayed'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   