# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_balances import SubscriptionGroupBalances
from advancedbilling.models.subscription_group_customer import SubscriptionGroupCustomer


class FullSubscriptionGroupResponse(object):

    """Implementation of the 'Full Subscription Group Response' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        scheme (int): TODO: type description here.
        customer_id (int): TODO: type description here.
        payment_profile_id (int): TODO: type description here.
        subscription_ids (List[int]): TODO: type description here.
        primary_subscription_id (int): TODO: type description here.
        next_assessment_at (str): TODO: type description here.
        state (str): TODO: type description here.
        cancel_at_end_of_period (bool): TODO: type description here.
        current_billing_amount_in_cents (int): TODO: type description here.
        customer (SubscriptionGroupCustomer): TODO: type description here.
        account_balances (SubscriptionGroupBalances): TODO: type description
            here.

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
        "current_billing_amount_in_cents": 'current_billing_amount_in_cents',
        "customer": 'customer',
        "account_balances": 'account_balances'
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
        'current_billing_amount_in_cents',
        'customer',
        'account_balances',
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
                 current_billing_amount_in_cents=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 account_balances=APIHelper.SKIP):
        """Constructor for the FullSubscriptionGroupResponse class"""

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
            self.next_assessment_at = next_assessment_at 
        if state is not APIHelper.SKIP:
            self.state = state 
        if cancel_at_end_of_period is not APIHelper.SKIP:
            self.cancel_at_end_of_period = cancel_at_end_of_period 
        if current_billing_amount_in_cents is not APIHelper.SKIP:
            self.current_billing_amount_in_cents = current_billing_amount_in_cents 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if account_balances is not APIHelper.SKIP:
            self.account_balances = account_balances 

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
        next_assessment_at = dictionary.get("next_assessment_at") if dictionary.get("next_assessment_at") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        cancel_at_end_of_period = dictionary.get("cancel_at_end_of_period") if "cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        current_billing_amount_in_cents = dictionary.get("current_billing_amount_in_cents") if dictionary.get("current_billing_amount_in_cents") else APIHelper.SKIP
        customer = SubscriptionGroupCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        account_balances = SubscriptionGroupBalances.from_dictionary(dictionary.get('account_balances')) if 'account_balances' in dictionary.keys() else APIHelper.SKIP
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
                   current_billing_amount_in_cents,
                   customer,
                   account_balances)
