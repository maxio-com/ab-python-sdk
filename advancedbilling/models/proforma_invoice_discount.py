# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.proforma_invoice_discount_breakout import ProformaInvoiceDiscountBreakout


class ProformaInvoiceDiscount(object):

    """Implementation of the 'Proforma Invoice Discount' model.

    TODO: type model description here.

    Attributes:
        title (str): TODO: type description here.
        source_type (str): TODO: type description here.
        discount_type (str): TODO: type description here.
        eligible_amount (str): TODO: type description here.
        discount_amount (str): TODO: type description here.
        line_item_breakouts (List[ProformaInvoiceDiscountBreakout]): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "source_type": 'source_type',
        "discount_type": 'discount_type',
        "eligible_amount": 'eligible_amount',
        "discount_amount": 'discount_amount',
        "line_item_breakouts": 'line_item_breakouts'
    }

    _optionals = [
        'title',
        'source_type',
        'discount_type',
        'eligible_amount',
        'discount_amount',
        'line_item_breakouts',
    ]

    def __init__(self,
                 title=APIHelper.SKIP,
                 source_type=APIHelper.SKIP,
                 discount_type=APIHelper.SKIP,
                 eligible_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP,
                 line_item_breakouts=APIHelper.SKIP):
        """Constructor for the ProformaInvoiceDiscount class"""

        # Initialize members of the class
        if title is not APIHelper.SKIP:
            self.title = title 
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if discount_type is not APIHelper.SKIP:
            self.discount_type = discount_type 
        if eligible_amount is not APIHelper.SKIP:
            self.eligible_amount = eligible_amount 
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount 
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
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        source_type = dictionary.get("source_type") if dictionary.get("source_type") else APIHelper.SKIP
        discount_type = dictionary.get("discount_type") if dictionary.get("discount_type") else APIHelper.SKIP
        eligible_amount = dictionary.get("eligible_amount") if dictionary.get("eligible_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        line_item_breakouts = None
        if dictionary.get('line_item_breakouts') is not None:
            line_item_breakouts = [ProformaInvoiceDiscountBreakout.from_dictionary(x) for x in dictionary.get('line_item_breakouts')]
        else:
            line_item_breakouts = APIHelper.SKIP
        # Return an object of this model
        return cls(title,
                   source_type,
                   discount_type,
                   eligible_amount,
                   discount_amount,
                   line_item_breakouts)
