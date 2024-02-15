# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_item import SubscriptionGroupItem


class SubscriptionGroupSignupResponse(object):

    """Implementation of the 'Subscription Group Signup Response' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        scheme (int): TODO: type description here.
        customer_id (int): TODO: type description here.
        payment_profile_id (int): TODO: type description here.
        subscription_ids (List[int]): TODO: type description here.
        primary_subscription_id (int): TODO: type description here.
        next_assessment_at (datetime): TODO: type description here.
        state (str): TODO: type description here.
        cancel_at_end_of_period (bool): TODO: type description here.
        subscriptions (List[SubscriptionGroupItem]): TODO: type description
            here.
        payment_collection_method (CollectionMethod): The type of payment
            collection to be used in the subscription. For legacy Statements
            Architecture valid options are - `invoice`, `automatic`. For
            current Relationship Invoicing Architecture valid options are -
            `remittance`, `automatic`, `prepaid`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "scheme": 'scheme',
        "customer_id": 'customer_id',
        "payment_profile_id": 'payment_profile_id',
        "subscription_ids": 'subscription_ids',
        "primary_subscription_id": 'primary_subscription_id',
        "next_assessment_at": 'next_assessment_at',
        "state": 'state',
        "cancel_at_end_of_period": 'cancel_at_end_of_period',
        "subscriptions": 'subscriptions',
        "payment_collection_method": 'payment_collection_method'
    }

    _optionals = [
        'uid',
        'scheme',
        'customer_id',
        'payment_profile_id',
        'subscription_ids',
        'primary_subscription_id',
        'next_assessment_at',
        'state',
        'cancel_at_end_of_period',
        'subscriptions',
        'payment_collection_method',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 scheme=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 payment_profile_id=APIHelper.SKIP,
                 subscription_ids=APIHelper.SKIP,
                 primary_subscription_id=APIHelper.SKIP,
                 next_assessment_at=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 cancel_at_end_of_period=APIHelper.SKIP,
                 subscriptions=APIHelper.SKIP,
                 payment_collection_method='automatic'):
        """Constructor for the SubscriptionGroupSignupResponse class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if scheme is not APIHelper.SKIP:
            self.scheme = scheme 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 
        if subscription_ids is not APIHelper.SKIP:
            self.subscription_ids = subscription_ids 
        if primary_subscription_id is not APIHelper.SKIP:
            self.primary_subscription_id = primary_subscription_id 
        if next_assessment_at is not APIHelper.SKIP:
            self.next_assessment_at = APIHelper.apply_datetime_converter(next_assessment_at, APIHelper.RFC3339DateTime) if next_assessment_at else None 
        if state is not APIHelper.SKIP:
            self.state = state 
        if cancel_at_end_of_period is not APIHelper.SKIP:
            self.cancel_at_end_of_period = cancel_at_end_of_period 
        if subscriptions is not APIHelper.SKIP:
            self.subscriptions = subscriptions 
        self.payment_collection_method = payment_collection_method 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        subscription_ids = dictionary.get("subscription_ids") if dictionary.get("subscription_ids") else APIHelper.SKIP
        primary_subscription_id = dictionary.get("primary_subscription_id") if dictionary.get("primary_subscription_id") else APIHelper.SKIP
        next_assessment_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_assessment_at")).datetime if dictionary.get("next_assessment_at") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        cancel_at_end_of_period = dictionary.get("cancel_at_end_of_period") if "cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        subscriptions = None
        if dictionary.get('subscriptions') is not None:
            subscriptions = [SubscriptionGroupItem.from_dictionary(x) for x in dictionary.get('subscriptions')]
        else:
            subscriptions = APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else 'automatic'
        # Return an object of this model
        return cls(uid,
                   scheme,
                   customer_id,
                   payment_profile_id,
                   subscription_ids,
                   primary_subscription_id,
                   next_assessment_at,
                   state,
                   cancel_at_end_of_period,
                   subscriptions,
                   payment_collection_method)
