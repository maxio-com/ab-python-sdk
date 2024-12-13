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
        id (int): TODO: type description here.
        subscription_group_uid (str): TODO: type description here.
        amount_in_cents (long|int): TODO: type description here.
        remaining_amount_in_cents (long|int): TODO: type description here.
        details (str): TODO: type description here.
        external (bool): TODO: type description here.
        memo (str): TODO: type description here.
        payment_type (PrepaymentMethod): TODO: type description here.
        created_at (datetime): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 created_at=APIHelper.SKIP,
                 additional_properties=None):
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
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        subscription_group_uid = dictionary.get("subscription_group_uid") if dictionary.get("subscription_group_uid") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        remaining_amount_in_cents = dictionary.get("remaining_amount_in_cents") if dictionary.get("remaining_amount_in_cents") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   subscription_group_uid,
                   amount_in_cents,
                   remaining_amount_in_cents,
                   details,
                   external,
                   memo,
                   payment_type,
                   created_at,
                   additional_properties)
