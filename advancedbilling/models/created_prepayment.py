# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreatedPrepayment(object):

    """Implementation of the 'Created Prepayment' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        subscription_id (int): TODO: type description here.
        amount_in_cents (long|int): TODO: type description here.
        memo (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        starting_balance_in_cents (long|int): TODO: type description here.
        ending_balance_in_cents (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "subscription_id": 'subscription_id',
        "amount_in_cents": 'amount_in_cents',
        "memo": 'memo',
        "created_at": 'created_at',
        "starting_balance_in_cents": 'starting_balance_in_cents',
        "ending_balance_in_cents": 'ending_balance_in_cents'
    }

    _optionals = [
        'id',
        'subscription_id',
        'amount_in_cents',
        'memo',
        'created_at',
        'starting_balance_in_cents',
        'ending_balance_in_cents',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 starting_balance_in_cents=APIHelper.SKIP,
                 ending_balance_in_cents=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreatedPrepayment class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if starting_balance_in_cents is not APIHelper.SKIP:
            self.starting_balance_in_cents = starting_balance_in_cents 
        if ending_balance_in_cents is not APIHelper.SKIP:
            self.ending_balance_in_cents = ending_balance_in_cents 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        starting_balance_in_cents = dictionary.get("starting_balance_in_cents") if dictionary.get("starting_balance_in_cents") else APIHelper.SKIP
        ending_balance_in_cents = dictionary.get("ending_balance_in_cents") if dictionary.get("ending_balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   subscription_id,
                   amount_in_cents,
                   memo,
                   created_at,
                   starting_balance_in_cents,
                   ending_balance_in_cents,
                   dictionary)
