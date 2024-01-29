# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.proforma_invoice_tax_breakout import ProformaInvoiceTaxBreakout


class ProformaInvoiceTax(object):

    """Implementation of the 'Proforma Invoice Tax' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        title (str): TODO: type description here.
        source_type (str): TODO: type description here.
        percentage (str): TODO: type description here.
        taxable_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.
        line_item_breakouts (List[ProformaInvoiceTaxBreakout]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "source_type": 'source_type',
        "percentage": 'percentage',
        "taxable_amount": 'taxable_amount',
        "tax_amount": 'tax_amount',
        "line_item_breakouts": 'line_item_breakouts'
    }

    _optionals = [
        'uid',
        'title',
        'source_type',
        'percentage',
        'taxable_amount',
        'tax_amount',
        'line_item_breakouts',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 source_type=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 line_item_breakouts=APIHelper.SKIP):
        """Constructor for the ProformaInvoiceTax class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if line_item_breakouts is not APIHelper.SKIP:
            self.line_item_breakouts = line_item_breakouts 

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
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        source_type = dictionary.get("source_type") if dictionary.get("source_type") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        line_item_breakouts = None
        if dictionary.get('line_item_breakouts') is not None:
            line_item_breakouts = [ProformaInvoiceTaxBreakout.from_dictionary(x) for x in dictionary.get('line_item_breakouts')]
        else:
            line_item_breakouts = APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   title,
                   source_type,
                   percentage,
                   taxable_amount,
                   tax_amount,
                   line_item_breakouts)
