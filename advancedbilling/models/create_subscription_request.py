# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_subscription import CreateSubscription


class CreateSubscriptionRequest(object):

    """Implementation of the 'Create Subscription Request' model.

    TODO: type model description here.

    Attributes:
        subscription (CreateSubscription): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription": 'subscription'
    }

    def __init__(self,
                 subscription=None):
        """Constructor for the CreateSubscriptionRequest class"""

        # Initialize members of the class
        self.subscription = subscription 

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
        subscription = CreateSubscription.from_dictionary(dictionary.get('subscription')) if dictionary.get('subscription') else None
        # Return an object of this model
        return cls(subscription)
