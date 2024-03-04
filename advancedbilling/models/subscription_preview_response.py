# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.subscription_preview import SubscriptionPreview


class SubscriptionPreviewResponse(object):

    """Implementation of the 'Subscription Preview Response' model.

    TODO: type model description here.

    Attributes:
        subscription_preview (SubscriptionPreview): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_preview": 'subscription_preview'
    }

    def __init__(self,
                 subscription_preview=None,
                 additional_properties={}):
        """Constructor for the SubscriptionPreviewResponse class"""

        # Initialize members of the class
        self.subscription_preview = subscription_preview 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        subscription_preview = SubscriptionPreview.from_dictionary(dictionary.get('subscription_preview')) if dictionary.get('subscription_preview') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(subscription_preview,
                   dictionary)
