# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProformaInvoiceDiscountBreakout(object):

    """Implementation of the 'Proforma Invoice Discount Breakout' model.

    TODO: type model description here.

    Attributes:
        eligible_amount (str): TODO: type description here.
        discount_amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "eligible_amount": 'eligible_amount',
        "discount_amount": 'discount_amount'
    }

    _optionals = [
        'eligible_amount',
        'discount_amount',
    ]

    def __init__(self,
                 eligible_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP):
        """Constructor for the ProformaInvoiceDiscountBreakout class"""

        # Initialize members of the class
        if eligible_amount is not APIHelper.SKIP:
            self.eligible_amount = eligible_amount 
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount 

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
        eligible_amount = dictionary.get("eligible_amount") if dictionary.get("eligible_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(eligible_amount,
                   discount_amount)
