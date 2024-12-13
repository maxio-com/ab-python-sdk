# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateOrUpdateEndpoint(object):

    """Implementation of the 'Create or Update Endpoint' model.

    Used to Create or Update Endpoint

    Attributes:
        url (str): TODO: type description here.
        webhook_subscriptions (List[WebhookSubscription]): TODO: type
            description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "webhook_subscriptions": 'webhook_subscriptions'
    }

    def __init__(self,
                 url=None,
                 webhook_subscriptions=None,
                 additional_properties=None):
        """Constructor for the CreateOrUpdateEndpoint class"""

        # Initialize members of the class
        self.url = url 
        self.webhook_subscriptions = webhook_subscriptions 

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
        url = dictionary.get("url") if dictionary.get("url") else None
        webhook_subscriptions = dictionary.get("webhook_subscriptions") if dictionary.get("webhook_subscriptions") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(url,
                   webhook_subscriptions,
                   additional_properties)
