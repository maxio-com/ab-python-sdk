# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.customer import Customer
from advancedbilling.models.subscription_group_signup_success_data import SubscriptionGroupSignupSuccessData


class SubscriptionGroupSignupSuccess(object):

    """Implementation of the 'Subscription Group Signup Success' model.

    TODO: type model description here.

    Attributes:
        subscription_group (SubscriptionGroupSignupSuccessData): TODO: type
            description here.
        customer (Customer): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_group": 'subscription_group',
        "customer": 'customer'
    }

    def __init__(self,
                 subscription_group=None,
                 customer=None):
        """Constructor for the SubscriptionGroupSignupSuccess class"""

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        subscription_group = SubscriptionGroupSignupSuccessData.from_dictionary(dictionary.get('subscription_group')) if dictionary.get('subscription_group') else None
        customer = Customer.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
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
            return APIHelper.is_valid_type(value=dictionary.subscription_group, type_callable=lambda value: SubscriptionGroupSignupSuccessData.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.customer, type_callable=lambda value: Customer.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('subscription_group'), type_callable=lambda value: SubscriptionGroupSignupSuccessData.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('customer'), type_callable=lambda value: Customer.validate(value))
