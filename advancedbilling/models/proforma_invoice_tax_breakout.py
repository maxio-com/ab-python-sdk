# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProformaInvoiceTaxBreakout(object):

    """Implementation of the 'Proforma Invoice Tax Breakout' model.

    TODO: type model description here.

    Attributes:
        taxable_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "taxable_amount": 'taxable_amount',
        "tax_amount": 'tax_amount'
    }

    _optionals = [
        'taxable_amount',
        'tax_amount',
    ]

    def __init__(self,
                 taxable_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP):
        """Constructor for the ProformaInvoiceTaxBreakout class"""

        # Initialize members of the class
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
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(taxable_amount,
                   tax_amount)
