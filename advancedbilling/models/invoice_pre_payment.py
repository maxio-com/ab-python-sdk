# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePrePayment(object):

    """Implementation of the 'Invoice PrePayment' model.

    TODO: type model description here.

    Attributes:
        subscription_id (int): The subscription id for the prepayment account
        amount_in_cents (long|int): The amount in cents of the prepayment that
            was created as a result of this payment.
        ending_balance_in_cents (long|int): The total balance of the
            prepayment account for this subscription including any prior
            prepayments
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 ending_balance_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoicePrePayment class"""

        # Initialize members of the class
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if ending_balance_in_cents is not APIHelper.SKIP:
            self.ending_balance_in_cents = ending_balance_in_cents 

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
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        ending_balance_in_cents = dictionary.get("ending_balance_in_cents") if dictionary.get("ending_balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscription_id,
                   amount_in_cents,
                   ending_balance_in_cents,
                   additional_properties)
