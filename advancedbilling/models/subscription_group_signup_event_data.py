# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.customer import Customer
from advancedbilling.models.subscription_group_signup_failure_data import SubscriptionGroupSignupFailureData


class SubscriptionGroupSignupEventData(object):

    """Implementation of the 'Subscription Group Signup Event Data' model.

    Attributes:
        subscription_group (SubscriptionGroupSignupFailureData): The model
            property of type SubscriptionGroupSignupFailureData.
        customer (Customer): The model property of type Customer.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 customer=None,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupSignupEventData class"""

        # Initialize members of the class
        self.subscription_group = subscription_group 
        self.customer = customer 

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
        subscription_group = SubscriptionGroupSignupFailureData.from_dictionary(dictionary.get('subscription_group')) if dictionary.get('subscription_group') else None
        customer = Customer.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscription_group,
                   customer,
                   additional_properties)

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
            return APIHelper.is_valid_type(value=dictionary.subscription_group,
                                           type_callable=lambda value: SubscriptionGroupSignupFailureData.validate(value),
                                           is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.customer,
                                            type_callable=lambda value: Customer.validate(value),
                                            is_value_nullable=True,
                                            is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('subscription_group'),
                                       type_callable=lambda value: SubscriptionGroupSignupFailureData.validate(value),
                                       is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('customer'),
                                        type_callable=lambda value: Customer.validate(value),
                                        is_value_nullable=True,
                                        is_model_dict=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_group={self.subscription_group!r}, '
                f'customer={self.customer!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_group={self.subscription_group!s}, '
                f'customer={self.customer!s}, '
                f'additional_properties={self.additional_properties!s})')
