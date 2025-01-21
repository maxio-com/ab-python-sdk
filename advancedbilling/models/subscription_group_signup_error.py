# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payer_error import PayerError
from advancedbilling.models.subscription_group_subscription_error import SubscriptionGroupSubscriptionError


class SubscriptionGroupSignupError(object):

    """Implementation of the 'Subscription Group Signup Error' model.

    Attributes:
        subscriptions (Dict[str, SubscriptionGroupSubscriptionError]): Object
            that as key have subscription position in request subscriptions
            array and as value subscription errors object.
        payer_reference (str): The model property of type str.
        payer (PayerError): The model property of type PayerError.
        subscription_group (List[str]): The model property of type List[str].
        payment_profile_id (str): The model property of type str.
        payer_id (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscriptions": 'subscriptions',
        "payer_reference": 'payer_reference',
        "payer": 'payer',
        "subscription_group": 'subscription_group',
        "payment_profile_id": 'payment_profile_id',
        "payer_id": 'payer_id'
    }

    _optionals = [
        'subscriptions',
        'payer_reference',
        'payer',
        'subscription_group',
        'payment_profile_id',
        'payer_id',
    ]

    def __init__(self,
                 subscriptions=APIHelper.SKIP,
                 payer_reference=APIHelper.SKIP,
                 payer=APIHelper.SKIP,
                 subscription_group=APIHelper.SKIP,
                 payment_profile_id=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupSignupError class"""

        # Initialize members of the class
        if subscriptions is not APIHelper.SKIP:
            self.subscriptions = subscriptions 
        if payer_reference is not APIHelper.SKIP:
            self.payer_reference = payer_reference 
        if payer is not APIHelper.SKIP:
            self.payer = payer 
        if subscription_group is not APIHelper.SKIP:
            self.subscription_group = subscription_group 
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 

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
        subscriptions = SubscriptionGroupSubscriptionError.from_dictionary(dictionary.get('subscriptions')) if 'subscriptions' in dictionary.keys() else APIHelper.SKIP
        payer_reference = dictionary.get("payer_reference") if dictionary.get("payer_reference") else APIHelper.SKIP
        payer = PayerError.from_dictionary(dictionary.get('payer')) if 'payer' in dictionary.keys() else APIHelper.SKIP
        subscription_group = dictionary.get("subscription_group") if dictionary.get("subscription_group") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        payer_id = dictionary.get("payer_id") if dictionary.get("payer_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscriptions,
                   payer_reference,
                   payer,
                   subscription_group,
                   payment_profile_id,
                   payer_id,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'subscriptions={self.subscriptions!r}, '
                f'payer_reference={self.payer_reference!r}, '
                f'payer={self.payer!r}, '
                f'subscription_group={self.subscription_group!r}, '
                f'payment_profile_id={self.payment_profile_id!r}, '
                f'payer_id={self.payer_id!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'subscriptions={self.subscriptions!s}, '
                f'payer_reference={self.payer_reference!s}, '
                f'payer={self.payer!s}, '
                f'subscription_group={self.subscription_group!s}, '
                f'payment_profile_id={self.payment_profile_id!s}, '
                f'payer_id={self.payer_id!s}, '
                f'additional_properties={self.additional_properties!s})')
