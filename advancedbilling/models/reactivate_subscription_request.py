# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.reactivation_billing import ReactivationBilling


class ReactivateSubscriptionRequest(object):

    """Implementation of the 'Reactivate Subscription Request' model.

    TODO: type model description here.

    Attributes:
        calendar_billing (ReactivationBilling): These values are only
            applicable to subscriptions using calendar billing
        include_trial (bool): If `true` is sent, the reactivated Subscription
            will include a trial if one is available. If `false` is sent, the
            trial period will be ignored.
        preserve_balance (bool): If `true` is passed, the existing
            subscription balance will NOT be cleared/reset before adding the
            additional reactivation charges.
        coupon_code (str): The coupon code to be applied during reactivation.
        use_credits_and_prepayments (bool): If true is sent, Chargify will use
            service credits and prepayments upon reactivation. If false is
            sent, the service credits and prepayments will be ignored.
        resume (bool | ResumeOptions | None): If `true`, Chargify will attempt
            to resume the subscription's billing period. if not resumable, the
            subscription will be reactivated with a new billing period. If
            `false`: Chargify will only attempt to reactivate the subscription.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "calendar_billing": 'calendar_billing',
        "include_trial": 'include_trial',
        "preserve_balance": 'preserve_balance',
        "coupon_code": 'coupon_code',
        "use_credits_and_prepayments": 'use_credits_and_prepayments',
        "resume": 'resume'
    }

    _optionals = [
        'calendar_billing',
        'include_trial',
        'preserve_balance',
        'coupon_code',
        'use_credits_and_prepayments',
        'resume',
    ]

    def __init__(self,
                 calendar_billing=APIHelper.SKIP,
                 include_trial=APIHelper.SKIP,
                 preserve_balance=APIHelper.SKIP,
                 coupon_code=APIHelper.SKIP,
                 use_credits_and_prepayments=APIHelper.SKIP,
                 resume=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ReactivateSubscriptionRequest class"""

        # Initialize members of the class
        if calendar_billing is not APIHelper.SKIP:
            self.calendar_billing = calendar_billing 
        if include_trial is not APIHelper.SKIP:
            self.include_trial = include_trial 
        if preserve_balance is not APIHelper.SKIP:
            self.preserve_balance = preserve_balance 
        if coupon_code is not APIHelper.SKIP:
            self.coupon_code = coupon_code 
        if use_credits_and_prepayments is not APIHelper.SKIP:
            self.use_credits_and_prepayments = use_credits_and_prepayments 
        if resume is not APIHelper.SKIP:
            self.resume = resume 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        calendar_billing = ReactivationBilling.from_dictionary(dictionary.get('calendar_billing')) if 'calendar_billing' in dictionary.keys() else APIHelper.SKIP
        include_trial = dictionary.get("include_trial") if "include_trial" in dictionary.keys() else APIHelper.SKIP
        preserve_balance = dictionary.get("preserve_balance") if "preserve_balance" in dictionary.keys() else APIHelper.SKIP
        coupon_code = dictionary.get("coupon_code") if dictionary.get("coupon_code") else APIHelper.SKIP
        use_credits_and_prepayments = dictionary.get("use_credits_and_prepayments") if "use_credits_and_prepayments" in dictionary.keys() else APIHelper.SKIP
        resume = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ReactivateSubscriptionRequestResume'), dictionary.get('resume'), False) if dictionary.get('resume') is not None else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(calendar_billing,
                   include_trial,
                   preserve_balance,
                   coupon_code,
                   use_credits_and_prepayments,
                   resume,
                   additional_properties)
