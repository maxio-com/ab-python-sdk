# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_subscription_group import CreateSubscriptionGroup


class CreateSubscriptionGroupRequest(object):

    """Implementation of the 'Create Subscription Group Request' model.

    TODO: type model description here.

    Attributes:
        subscription_group (CreateSubscriptionGroup): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_group": 'subscription_group'
    }

    def __init__(self,
                 subscription_group=None):
        """Constructor for the CreateSubscriptionGroupRequest class"""

        # Initialize members of the class
        self.subscription_group = subscription_group 

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
        subscription_group = CreateSubscriptionGroup.from_dictionary(dictionary.get('subscription_group')) if dictionary.get('subscription_group') else None
        # Return an object of this model
        return cls(subscription_group)
