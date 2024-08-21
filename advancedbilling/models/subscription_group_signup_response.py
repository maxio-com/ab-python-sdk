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
        state (SubscriptionState): The state of a subscription. * **Live
            States**     * `active` - A normal, active subscription. It is not
            in a trial and is paid and up to date.     * `assessing` - An
            internal (transient) state that indicates a subscription is in the
            middle of periodic assessment. Do not base any access decisions in
            your app on this state, as it may not always be exposed.     *
            `pending` - An internal (transient) state that indicates a
            subscription is in the creation process. Do not base any access
            decisions in your app on this state, as it may not always be
            exposed.     * `trialing` - A subscription in trialing state has a
            valid trial subscription. This type of subscription may transition
            to active once payment is received when the trial has ended.
            Otherwise, it may go to a Problem or End of Life state.     *
            `paused` - An internal state that indicates that your account with
            Advanced Billing is in arrears. * **Problem States**     *
            `past_due` - Indicates that the most recent payment has failed,
            and payment is past due for this subscription. If you have enabled
            our automated dunning, this subscription will be in the dunning
            process (additional status and callbacks from the dunning process
            will be available in the future). If you are handling dunning and
            payment updates yourself, you will want to use this state to
            initiate a payment update from your customers.     *
            `soft_failure` - Indicates that normal assessment/processing of
            the subscription has failed for a reason that cannot be fixed by
            the Customer. For example, a Soft Fail may result from a timeout
            at the gateway or incorrect credentials on your part. The
            subscriptions should be retried automatically. An interface is
            being built for you to review problems resulting from these events
            to take manual action when needed.     * `unpaid` - Indicates an
            unpaid subscription. A subscription is marked unpaid if the retry
            period expires and you have configured your
            [Dunning](https://maxio.zendesk.com/hc/en-us/articles/2428707658356
            5-Dunning-Overview) settings to have a Final Action of `mark the
            subscription unpaid`. * **End of Life States**     * `canceled` -
            Indicates a canceled subscription. This may happen at your request
            (via the API or the web interface) or due to the expiration of the
            [Dunning](https://maxio.zendesk.com/hc/en-us/articles/2428707658356
            5-Dunning-Overview) process without payment. See the
            [Reactivation](https://maxio.zendesk.com/hc/en-us/articles/24252109
            503629-Reactivating-and-Resuming) documentation for info on how to
            restart a canceled subscription.     While a subscription is
            canceled, its period will not advance, it will not accrue any new
            charges, and Advanced Billing will not attempt to collect the
            overdue balance.     * `expired` - Indicates a subscription that
            has expired due to running its normal life cycle. Some products
            may be configured to have an expiration period. An expired
            subscription then is one that stayed active until it fulfilled its
            full period.     * `failed_to_create` - Indicates that signup has
            failed. (You may see this state in a signup_failure webhook.)    
            * `on_hold` - Indicates that a subscription’s billing has been
            temporarily stopped. While it is expected that the subscription
            will resume and return to active status, this is still treated as
            an “End of Life” state because the customer is not paying for
            services during this time.     * `suspended` - Indicates that a
            prepaid subscription has used up all their prepayment balance. If
            a prepayment is applied, it will return to an active state.     *
            `trial_ended` - A subscription in a trial_ended state is a
            subscription that completed a no-obligation trial and did not have
            a card on file at the expiration of the trial period. See [Product
            Pricing – No Obligation
            Trials](https://maxio.zendesk.com/hc/en-us/articles/24261076617869-
            Product-Editing) for more details.  See [Subscription
            States](https://maxio.zendesk.com/hc/en-us/articles/24252119027853-
            Subscription-States) for more info about subscription states and
            state transitions.
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
                 payment_collection_method=APIHelper.SKIP,
                 additional_properties={}):
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
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method 

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
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
                   payment_collection_method,
                   dictionary)
