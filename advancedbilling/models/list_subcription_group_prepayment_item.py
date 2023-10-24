# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListSubcriptionGroupPrepaymentItem(object):

    """Implementation of the 'List Subcription Group Prepayment Item' model.

    TODO: type model description here.

    Attributes:
        id (float): TODO: type description here.
        subscription_group_uid (str): TODO: type description here.
        amount_in_cents (float): TODO: type description here.
        remaining_amount_in_cents (float): TODO: type description here.
        details (str): TODO: type description here.
        external (bool): TODO: type description here.
        memo (str): TODO: type description here.
        payment_type (PrepaymentMethod): :- When the `method` specified is
            `"credit_card_on_file"`, the prepayment amount will be collected
            using the default credit card payment profile and applied to the
            prepayment account balance. This is especially useful for manual
            replenishment of prepaid subscriptions.
        created_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "subscription_group_uid": 'subscription_group_uid',
        "amount_in_cents": 'amount_in_cents',
        "remaining_amount_in_cents": 'remaining_amount_in_cents',
        "details": 'details',
        "external": 'external',
        "memo": 'memo',
        "payment_type": 'payment_type',
        "created_at": 'created_at'
    }

    _optionals = [
        'id',
        'subscription_group_uid',
        'amount_in_cents',
        'remaining_amount_in_cents',
        'details',
        'external',
        'memo',
        'payment_type',
        'created_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 subscription_group_uid=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 remaining_amount_in_cents=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 external=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 created_at=APIHelper.SKIP):
        """Constructor for the ListSubcriptionGroupPrepaymentItem class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if subscription_group_uid is not APIHelper.SKIP:
            self.subscription_group_uid = subscription_group_uid 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if remaining_amount_in_cents is not APIHelper.SKIP:
            self.remaining_amount_in_cents = remaining_amount_in_cents 
        if details is not APIHelper.SKIP:
            self.details = details 
        if external is not APIHelper.SKIP:
            self.external = external 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        subscription_group_uid = dictionary.get("subscription_group_uid") if dictionary.get("subscription_group_uid") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        remaining_amount_in_cents = dictionary.get("remaining_amount_in_cents") if dictionary.get("remaining_amount_in_cents") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   subscription_group_uid,
                   amount_in_cents,
                   remaining_amount_in_cents,
                   details,
                   external,
                   memo,
                   payment_type,
                   created_at)
