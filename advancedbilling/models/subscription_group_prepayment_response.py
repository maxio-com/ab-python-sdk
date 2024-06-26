# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupPrepaymentResponse(object):

    """Implementation of the 'Subscription Group Prepayment Response' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        amount_in_cents (long|int): The amount in cents of the entry.
        ending_balance_in_cents (long|int): The ending balance in cents of the
            account.
        entry_type (ServiceCreditType): The type of entry
        memo (str): A memo attached to the entry.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "amount_in_cents": 'amount_in_cents',
        "ending_balance_in_cents": 'ending_balance_in_cents',
        "entry_type": 'entry_type',
        "memo": 'memo'
    }

    _optionals = [
        'id',
        'amount_in_cents',
        'ending_balance_in_cents',
        'entry_type',
        'memo',
    ]

    _nullables = [
        'memo',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 ending_balance_in_cents=APIHelper.SKIP,
                 entry_type=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the SubscriptionGroupPrepaymentResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if ending_balance_in_cents is not APIHelper.SKIP:
            self.ending_balance_in_cents = ending_balance_in_cents 
        if entry_type is not APIHelper.SKIP:
            self.entry_type = entry_type 
        if memo is not APIHelper.SKIP:
            self.memo = memo 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        ending_balance_in_cents = dictionary.get("ending_balance_in_cents") if dictionary.get("ending_balance_in_cents") else APIHelper.SKIP
        entry_type = dictionary.get("entry_type") if dictionary.get("entry_type") else APIHelper.SKIP
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   amount_in_cents,
                   ending_balance_in_cents,
                   entry_type,
                   memo,
                   dictionary)
