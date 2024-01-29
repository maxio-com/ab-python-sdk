# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionStateChange(object):

    """Implementation of the 'Subscription State Change' model.

    TODO: type model description here.

    Attributes:
        previous_subscription_state (str): TODO: type description here.
        new_subscription_state (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_subscription_state": 'previous_subscription_state',
        "new_subscription_state": 'new_subscription_state'
    }

    def __init__(self,
                 previous_subscription_state=None,
                 new_subscription_state=None):
        """Constructor for the SubscriptionStateChange class"""

        # Initialize members of the class
        self.previous_subscription_state = previous_subscription_state 
        self.new_subscription_state = new_subscription_state 

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
        previous_subscription_state = dictionary.get("previous_subscription_state") if dictionary.get("previous_subscription_state") else None
        new_subscription_state = dictionary.get("new_subscription_state") if dictionary.get("new_subscription_state") else None
        # Return an object of this model
        return cls(previous_subscription_state,
                   new_subscription_state)

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
            return APIHelper.is_valid_type(value=dictionary.previous_subscription_state, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.new_subscription_state, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('previous_subscription_state'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('new_subscription_state'), type_callable=lambda value: isinstance(value, str))
