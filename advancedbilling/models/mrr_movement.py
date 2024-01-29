# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class MRRMovement(object):

    """Implementation of the 'MRR Movement' model.

    TODO: type model description here.

    Attributes:
        amount (int): TODO: type description here.
        category (str): TODO: type description here.
        subscriber_delta (int): TODO: type description here.
        lead_delta (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "category": 'category',
        "subscriber_delta": 'subscriber_delta',
        "lead_delta": 'lead_delta'
    }

    _optionals = [
        'amount',
        'category',
        'subscriber_delta',
        'lead_delta',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 subscriber_delta=APIHelper.SKIP,
                 lead_delta=APIHelper.SKIP):
        """Constructor for the MRRMovement class"""

        # Initialize members of the class
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if category is not APIHelper.SKIP:
            self.category = category 
        if subscriber_delta is not APIHelper.SKIP:
            self.subscriber_delta = subscriber_delta 
        if lead_delta is not APIHelper.SKIP:
            self.lead_delta = lead_delta 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        category = dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        subscriber_delta = dictionary.get("subscriber_delta") if dictionary.get("subscriber_delta") else APIHelper.SKIP
        lead_delta = dictionary.get("lead_delta") if dictionary.get("lead_delta") else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   category,
                   subscriber_delta,
                   lead_delta)
