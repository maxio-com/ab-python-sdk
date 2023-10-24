# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PrePayment(object):

    """Implementation of the 'Pre-Payment' model.

    TODO: type model description here.

    Attributes:
        subscription_id (str): The subscription id for the prepayment account
        amount_in_cents (str): The amount in cents of the prepayment that was
            created as a result of this payment.
        ending_balance_in_cents (str): The total balance of the prepayment
            account for this subscription including any prior prepayments

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": 'subscription_id',
        "amount_in_cents": 'amount_in_cents',
        "ending_balance_in_cents": 'ending_balance_in_cents'
    }

    _optionals = [
        'subscription_id',
        'amount_in_cents',
        'ending_balance_in_cents',
    ]

    def __init__(self,
                 subscription_id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 ending_balance_in_cents=APIHelper.SKIP):
        """Constructor for the PrePayment class"""

        # Initialize members of the class
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if ending_balance_in_cents is not APIHelper.SKIP:
            self.ending_balance_in_cents = ending_balance_in_cents 

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
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        ending_balance_in_cents = dictionary.get("ending_balance_in_cents") if dictionary.get("ending_balance_in_cents") else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription_id,
                   amount_in_cents,
                   ending_balance_in_cents)
