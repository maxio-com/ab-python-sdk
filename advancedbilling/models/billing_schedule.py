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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_billing_at": 'initial_billing_at'
    }

    _optionals = [
        'initial_billing_at',
    ]

    def __init__(self,
                 initial_billing_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the BillingSchedule class"""

        # Initialize members of the class
        if initial_billing_at is not APIHelper.SKIP:
            self.initial_billing_at = initial_billing_at 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        initial_billing_at = dateutil.parser.parse(dictionary.get('initial_billing_at')).date() if dictionary.get('initial_billing_at') else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(initial_billing_at,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
