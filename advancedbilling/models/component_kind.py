# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ComponentKind(object):

    """Implementation of the 'Component Kind' enum.

    A handle for the component type

    Attributes:
        METERED_COMPONENT: TODO: type description here.
        QUANTITY_BASED_COMPONENT: TODO: type description here.
        ON_OFF_COMPONENT: TODO: type description here.
        PREPAID_USAGE_COMPONENT: TODO: type description here.
        EVENT_BASED_COMPONENT: TODO: type description here.

    """
    _all_values = ['metered_component', 'quantity_based_component', 'on_off_component', 'prepaid_usage_component', 'event_based_component']
    METERED_COMPONENT = 'metered_component'

    QUANTITY_BASED_COMPONENT = 'quantity_based_component'

    ON_OFF_COMPONENT = 'on_off_component'

    PREPAID_USAGE_COMPONENT = 'prepaid_usage_component'

    EVENT_BASED_COMPONENT = 'event_based_component'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
