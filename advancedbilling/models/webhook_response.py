# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.webhook import Webhook


class WebhookResponse(object):

    """Implementation of the 'Webhook Response' model.

    TODO: type model description here.

    Attributes:
        webhook (Webhook): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "webhook": 'webhook'
    }

    _optionals = [
        'webhook',
    ]

    def __init__(self,
                 webhook=APIHelper.SKIP):
        """Constructor for the WebhookResponse class"""

        # Initialize members of the class
        if webhook is not APIHelper.SKIP:
            self.webhook = webhook 

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
        webhook = Webhook.from_dictionary(dictionary.get('webhook')) if 'webhook' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(webhook)
