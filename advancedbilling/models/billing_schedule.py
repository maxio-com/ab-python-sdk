# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class BillingSchedule(object):

    """Implementation of the 'Billing Schedule' model.

    This attribute is particularly useful when you need to align billing
    events for different components on distinct schedules within a
    subscription. Please note this only works for site with Multifrequency
    enabled

    Attributes:
        initial_billing_at (date): The initial_billing_at attribute in Maxio
            allows you to specify a custom starting date for billing cycles
            associated with components that have their own billing frequency
            set. Only ISO8601 format is supported.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_billing_at": 'initial_billing_at'
    }

    _optionals = [
        'initial_billing_at',
    ]

    def __init__(self,
                 initial_billing_at=APIHelper.SKIP):
        """Constructor for the BillingSchedule class"""

        # Initialize members of the class
        if initial_billing_at is not APIHelper.SKIP:
            self.initial_billing_at = initial_billing_at 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        initial_billing_at = dateutil.parser.parse(dictionary.get('initial_billing_at')).date() if dictionary.get('initial_billing_at') else APIHelper.SKIP
        # Return an object of this model
        return cls(initial_billing_at)
