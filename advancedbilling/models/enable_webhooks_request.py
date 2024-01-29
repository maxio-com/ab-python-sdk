# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class EnableWebhooksRequest(object):

    """Implementation of the 'Enable Webhooks Request' model.

    TODO: type model description here.

    Attributes:
        webhooks_enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "webhooks_enabled": 'webhooks_enabled'
    }

    def __init__(self,
                 webhooks_enabled=None):
        """Constructor for the EnableWebhooksRequest class"""

        # Initialize members of the class
        self.webhooks_enabled = webhooks_enabled 

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
        webhooks_enabled = dictionary.get("webhooks_enabled") if "webhooks_enabled" in dictionary.keys() else None
        # Return an object of this model
        return cls(webhooks_enabled)
