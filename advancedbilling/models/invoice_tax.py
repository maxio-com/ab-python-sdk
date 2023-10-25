# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_tax_breakout import InvoiceTaxBreakout
from advancedbilling.models.invoice_tax_component_breakout import InvoiceTaxComponentBreakout


class InvoiceTax(object):

    """Implementation of the 'Invoice Tax' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        title (str): TODO: type description here.
        description (str): TODO: type description here.
        source_type (str): TODO: type description here.
        source_id (int): TODO: type description here.
        percentage (str): TODO: type description here.
        taxable_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.
        transaction_id (int): TODO: type description here.
        line_item_breakouts (List[InvoiceTaxBreakout]): TODO: type description
            here.
        tax_component_breakouts (List[InvoiceTaxComponentBreakout]): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "description": 'description',
        "source_type": 'source_type',
        "source_id": 'source_id',
        "percentage": 'percentage',
        "taxable_amount": 'taxable_amount',
        "tax_amount": 'tax_amount',
        "transaction_id": 'transaction_id',
        "line_item_breakouts": 'line_item_breakouts',
        "tax_component_breakouts": 'tax_component_breakouts'
    }

    _optionals = [
        'uid',
        'title',
        'description',
        'source_type',
        'source_id',
        'percentage',
        'taxable_amount',
        'tax_amount',
        'transaction_id',
        'line_item_breakouts',
        'tax_component_breakouts',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 source_type=APIHelper.SKIP,
                 source_id=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 line_item_breakouts=APIHelper.SKIP,
                 tax_component_breakouts=APIHelper.SKIP):
        """Constructor for the InvoiceTax class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if source_id is not APIHelper.SKIP:
            self.source_id = source_id 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if line_item_breakouts is not APIHelper.SKIP:
            self.line_item_breakouts = line_item_breakouts 
        if tax_component_breakouts is not APIHelper.SKIP:
            self.tax_component_breakouts = tax_component_breakouts 

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        source_type = dictionary.get("source_type") if dictionary.get("source_type") else APIHelper.SKIP
        source_id = dictionary.get("source_id") if dictionary.get("source_id") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        line_item_breakouts = None
        if dictionary.get('line_item_breakouts') is not None:
            line_item_breakouts = [InvoiceTaxBreakout.from_dictionary(x) for x in dictionary.get('line_item_breakouts')]
        else:
            line_item_breakouts = APIHelper.SKIP
        tax_component_breakouts = None
        if dictionary.get('tax_component_breakouts') is not None:
            tax_component_breakouts = [InvoiceTaxComponentBreakout.from_dictionary(x) for x in dictionary.get('tax_component_breakouts')]
        else:
            tax_component_breakouts = APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   title,
                   description,
                   source_type,
                   source_id,
                   percentage,
                   taxable_amount,
                   tax_amount,
                   transaction_id,
                   line_item_breakouts,
                   tax_component_breakouts)
