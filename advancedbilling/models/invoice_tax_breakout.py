# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceTaxBreakout(object):

    """Implementation of the 'Invoice Tax Breakout' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        taxable_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "taxable_amount": 'taxable_amount',
        "tax_amount": 'tax_amount'
    }

    _optionals = [
        'uid',
        'taxable_amount',
        'tax_amount',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP):
        """Constructor for the InvoiceTaxBreakout class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 

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
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   taxable_amount,
                   tax_amount)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
