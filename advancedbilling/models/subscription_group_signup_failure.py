# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_signup_failure_data import SubscriptionGroupSignupFailureData


class SubscriptionGroupSignupFailure(object):

    """Implementation of the 'Subscription Group Signup Failure' model.

    TODO: type model description here.

    Attributes:
        subscription_group (SubscriptionGroupSignupFailureData): TODO: type
            description here.
        customer (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_group": 'subscription_group',
        "customer": 'customer'
    }

    _nullables = [
        'customer',
    ]

    def __init__(self,
                 subscription_group=None,
                 customer=None):
        """Constructor for the SubscriptionGroupSignupFailure class"""

        # Initialize members of the class
        self.subscription_group = subscription_group 
        self.customer = customer 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        subscription_group = SubscriptionGroupSignupFailureData.from_dictionary(dictionary.get('subscription_group')) if dictionary.get('subscription_group') else None
        customer = dictionary.get("customer") if dictionary.get("customer") else None
        # Return an object of this model
        return cls(subscription_group,
                   customer)

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
            return APIHelper.is_valid_type(value=dictionary.subscription_group, type_callable=lambda value: SubscriptionGroupSignupFailureData.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.customer, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('subscription_group'), type_callable=lambda value: SubscriptionGroupSignupFailureData.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('customer'), type_callable=lambda value: isinstance(value, str))
