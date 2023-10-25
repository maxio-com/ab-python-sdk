# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Prepayment1(object):

    """Implementation of the 'Prepayment1' model.

    TODO: type model description here.

    Attributes:
        id (float): TODO: type description here.
        subscription_id (float): TODO: type description here.
        amount_in_cents (float): TODO: type description here.
        remaining_amount_in_cents (float): TODO: type description here.
        refunded_amount_in_cents (float): TODO: type description here.
        details (str): TODO: type description here.
        external (bool): TODO: type description here.
        memo (str): TODO: type description here.
        payment_type (PrepaymentMethod): The payment type of the prepayment.
        created_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "subscription_id": 'subscription_id',
        "amount_in_cents": 'amount_in_cents',
        "remaining_amount_in_cents": 'remaining_amount_in_cents',
        "external": 'external',
        "memo": 'memo',
        "created_at": 'created_at',
        "refunded_amount_in_cents": 'refunded_amount_in_cents',
        "details": 'details',
        "payment_type": 'payment_type'
    }

    _optionals = [
        'refunded_amount_in_cents',
        'details',
        'payment_type',
    ]

    def __init__(self,
                 id=None,
                 subscription_id=None,
                 amount_in_cents=None,
                 remaining_amount_in_cents=None,
                 external=None,
                 memo=None,
                 created_at=None,
                 refunded_amount_in_cents=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP):
        """Constructor for the Prepayment1 class"""

        # Initialize members of the class
        self.id = id 
        self.subscription_id = subscription_id 
        self.amount_in_cents = amount_in_cents 
        self.remaining_amount_in_cents = remaining_amount_in_cents 
        if refunded_amount_in_cents is not APIHelper.SKIP:
            self.refunded_amount_in_cents = refunded_amount_in_cents 
        if details is not APIHelper.SKIP:
            self.details = details 
        self.external = external 
        self.memo = memo 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
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
        id = dictionary.get("id") if dictionary.get("id") else None
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        remaining_amount_in_cents = dictionary.get("remaining_amount_in_cents") if dictionary.get("remaining_amount_in_cents") else None
        external = dictionary.get("external") if "external" in dictionary.keys() else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else None
        refunded_amount_in_cents = dictionary.get("refunded_amount_in_cents") if dictionary.get("refunded_amount_in_cents") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   subscription_id,
                   amount_in_cents,
                   remaining_amount_in_cents,
                   external,
                   memo,
                   created_at,
                   refunded_amount_in_cents,
                   details,
                   payment_type)
