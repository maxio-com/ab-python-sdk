# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class EnableWebhooksResponse(object):

    """Implementation of the 'Enable Webhooks Response' model.

    TODO: type model description here.

    Attributes:
        webhooks_enabled (bool): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "webhooks_enabled": 'webhooks_enabled'
    }

    _optionals = [
        'webhooks_enabled',
    ]

    def __init__(self,
                 webhooks_enabled=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the EnableWebhooksResponse class"""

        # Initialize members of the class
        if webhooks_enabled is not APIHelper.SKIP:
            self.webhooks_enabled = webhooks_enabled 

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
        webhooks_enabled = dictionary.get("webhooks_enabled") if "webhooks_enabled" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(webhooks_enabled,
                   additional_properties)
