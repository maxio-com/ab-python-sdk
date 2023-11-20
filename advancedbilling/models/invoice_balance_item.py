# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceBalanceItem(object):

    """Implementation of the 'Invoice Balance Item' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        number (str): TODO: type description here.
        outstanding_amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "number": 'number',
        "outstanding_amount": 'outstanding_amount'
    }

    _optionals = [
        'uid',
        'number',
        'outstanding_amount',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 outstanding_amount=APIHelper.SKIP):
        """Constructor for the InvoiceBalanceItem class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if number is not APIHelper.SKIP:
            self.number = number 
        if outstanding_amount is not APIHelper.SKIP:
            self.outstanding_amount = outstanding_amount 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        outstanding_amount = dictionary.get("outstanding_amount") if dictionary.get("outstanding_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   number,
                   outstanding_amount)
