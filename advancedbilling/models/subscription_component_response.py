# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_component import SubscriptionComponent


class SubscriptionComponentResponse(object):

    """Implementation of the 'Subscription Component Response' model.

    TODO: type model description here.

    Attributes:
        component (SubscriptionComponent): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component": 'component'
    }

    _optionals = [
        'component',
    ]

    def __init__(self,
                 component=APIHelper.SKIP):
        """Constructor for the SubscriptionComponentResponse class"""

        # Initialize members of the class
        if component is not APIHelper.SKIP:
            self.component = component 

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
        component = SubscriptionComponent.from_dictionary(dictionary.get('component')) if 'component' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(component)
