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

    TODO: type model description here.

    Attributes:
        subscriptions (Dict[str, SubscriptionGroupSubscriptionError]): Object
            that as key have subscription position in request subscriptions
            array and as value subscription errors object.
        payer_reference (str): TODO: type description here.
        payer (PayerError): TODO: type description here.
        subscription_group (List[str]): TODO: type description here.
        payment_profile_id (str): TODO: type description here.
        payer_id (str): TODO: type description here.

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
                 payer_id=APIHelper.SKIP):
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
        subscriptions = SubscriptionGroupSubscriptionError.from_dictionary(dictionary.get('subscriptions')) if 'subscriptions' in dictionary.keys() else APIHelper.SKIP
        payer_reference = dictionary.get("payer_reference") if dictionary.get("payer_reference") else APIHelper.SKIP
        payer = PayerError.from_dictionary(dictionary.get('payer')) if 'payer' in dictionary.keys() else APIHelper.SKIP
        subscription_group = dictionary.get("subscription_group") if dictionary.get("subscription_group") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        payer_id = dictionary.get("payer_id") if dictionary.get("payer_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(subscriptions,
                   payer_reference,
                   payer,
                   subscription_group,
                   payment_profile_id,
                   payer_id)
