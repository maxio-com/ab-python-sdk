# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProformaInvoicePayment(object):

    """Implementation of the 'Proforma Invoice Payment' model.

    TODO: type model description here.

    Attributes:
        memo (str): TODO: type description here.
        original_amount (str): TODO: type description here.
        applied_amount (str): TODO: type description here.
        prepayment (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "prepayment": 'prepayment'
    }

    _optionals = [
        'memo',
        'original_amount',
        'applied_amount',
        'prepayment',
    ]

    def __init__(self,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP):
        """Constructor for the ProformaInvoicePayment class"""

        # Initialize members of the class
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 

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
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(memo,
                   original_amount,
                   applied_amount,
                   prepayment)
