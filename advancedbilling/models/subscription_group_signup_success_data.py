# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupSignupSuccessData(object):

    """Implementation of the 'Subscription Group Signup Success Data' model.

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
        "cancel_at_end_of_period": 'cancel_at_end_of_period'
    }

    def __init__(self,
                 uid=None,
                 scheme=None,
                 customer_id=None,
                 payment_profile_id=None,
                 subscription_ids=None,
                 primary_subscription_id=None,
                 next_assessment_at=None,
                 state=None,
                 cancel_at_end_of_period=None):
        """Constructor for the SubscriptionGroupSignupSuccessData class"""

        # Initialize members of the class
        self.uid = uid 
        self.scheme = scheme 
        self.customer_id = customer_id 
        self.payment_profile_id = payment_profile_id 
        self.subscription_ids = subscription_ids 
        self.primary_subscription_id = primary_subscription_id 
        self.next_assessment_at = next_assessment_at 
        self.state = state 
        self.cancel_at_end_of_period = cancel_at_end_of_period 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else None
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else None
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else None
        subscription_ids = dictionary.get("subscription_ids") if dictionary.get("subscription_ids") else None
        primary_subscription_id = dictionary.get("primary_subscription_id") if dictionary.get("primary_subscription_id") else None
        next_assessment_at = dictionary.get("next_assessment_at") if dictionary.get("next_assessment_at") else None
        state = dictionary.get("state") if dictionary.get("state") else None
        cancel_at_end_of_period = dictionary.get("cancel_at_end_of_period") if "cancel_at_end_of_period" in dictionary.keys() else None
        # Return an object of this model
        return cls(uid,
                   scheme,
                   customer_id,
                   payment_profile_id,
                   subscription_ids,
                   primary_subscription_id,
                   next_assessment_at,
                   state,
                   cancel_at_end_of_period)

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
            return APIHelper.is_valid_type(value=dictionary.uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.scheme, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.customer_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.payment_profile_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.subscription_ids, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.primary_subscription_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.next_assessment_at, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.state, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.cancel_at_end_of_period, type_callable=lambda value: isinstance(value, bool))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('scheme'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('customer_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_profile_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('subscription_ids'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('primary_subscription_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('next_assessment_at'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('state'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('cancel_at_end_of_period'), type_callable=lambda value: isinstance(value, bool))
