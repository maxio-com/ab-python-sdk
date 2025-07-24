# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_balances import SubscriptionGroupBalances


class ListSubscriptionGroupsItem(object):

    """Implementation of the 'List Subscription Groups Item' model.

    Attributes:
        uid (str): The model property of type str.
        scheme (int): The model property of type int.
        customer_id (int): The model property of type int.
        payment_profile_id (int): The model property of type int.
        subscription_ids (List[int]): The model property of type List[int].
        primary_subscription_id (int): The model property of type int.
        next_assessment_at (datetime): The model property of type datetime.
        state (str): The model property of type str.
        cancel_at_end_of_period (bool): The model property of type bool.
        account_balances (SubscriptionGroupBalances): The model property of
            type SubscriptionGroupBalances.
        group_type (GroupType): The model property of type GroupType.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        "account_balances": 'account_balances',
        "group_type": 'group_type'
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
        'account_balances',
        'group_type',
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
                 account_balances=APIHelper.SKIP,
                 group_type=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListSubscriptionGroupsItem class"""

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
        if account_balances is not APIHelper.SKIP:
            self.account_balances = account_balances 
        if group_type is not APIHelper.SKIP:
            self.group_type = group_type 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        subscription_ids = dictionary.get("subscription_ids") if dictionary.get("subscription_ids") else APIHelper.SKIP
        primary_subscription_id = dictionary.get("primary_subscription_id") if dictionary.get("primary_subscription_id") else APIHelper.SKIP
        next_assessment_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_assessment_at")).datetime if dictionary.get("next_assessment_at") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        cancel_at_end_of_period = dictionary.get("cancel_at_end_of_period") if "cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        account_balances = SubscriptionGroupBalances.from_dictionary(dictionary.get('account_balances')) if 'account_balances' in dictionary.keys() else APIHelper.SKIP
        group_type = dictionary.get("group_type") if dictionary.get("group_type") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   account_balances,
                   group_type,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'scheme={(self.scheme if hasattr(self, "scheme") else None)!r}, '
                f'customer_id={(self.customer_id if hasattr(self, "customer_id") else None)!r}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!r}, '
                f'subscription_ids={(self.subscription_ids if hasattr(self, "subscription_ids") else None)!r}, '
                f'primary_subscription_id={(self.primary_subscription_id if hasattr(self, "primary_subscription_id") else None)!r}, '
                f'next_assessment_at={(self.next_assessment_at if hasattr(self, "next_assessment_at") else None)!r}, '
                f'state={(self.state if hasattr(self, "state") else None)!r}, '
                f'cancel_at_end_of_period={(self.cancel_at_end_of_period if hasattr(self, "cancel_at_end_of_period") else None)!r}, '
                f'account_balances={(self.account_balances if hasattr(self, "account_balances") else None)!r}, '
                f'group_type={(self.group_type if hasattr(self, "group_type") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'scheme={(self.scheme if hasattr(self, "scheme") else None)!s}, '
                f'customer_id={(self.customer_id if hasattr(self, "customer_id") else None)!s}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!s}, '
                f'subscription_ids={(self.subscription_ids if hasattr(self, "subscription_ids") else None)!s}, '
                f'primary_subscription_id={(self.primary_subscription_id if hasattr(self, "primary_subscription_id") else None)!s}, '
                f'next_assessment_at={(self.next_assessment_at if hasattr(self, "next_assessment_at") else None)!s}, '
                f'state={(self.state if hasattr(self, "state") else None)!s}, '
                f'cancel_at_end_of_period={(self.cancel_at_end_of_period if hasattr(self, "cancel_at_end_of_period") else None)!s}, '
                f'account_balances={(self.account_balances if hasattr(self, "account_balances") else None)!s}, '
                f'group_type={(self.group_type if hasattr(self, "group_type") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
