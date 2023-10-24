# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_balance_item import InvoiceBalanceItem


class InvoicePreviousBalance(object):

    """Implementation of the 'Invoice Previous Balance' model.

    TODO: type model description here.

    Attributes:
        capture_date (str): TODO: type description here.
        invoices (List[InvoiceBalanceItem]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capture_date": 'capture_date',
        "invoices": 'invoices'
    }

    _optionals = [
        'capture_date',
        'invoices',
    ]

    def __init__(self,
                 capture_date=APIHelper.SKIP,
                 invoices=APIHelper.SKIP):
        """Constructor for the InvoicePreviousBalance class"""

        # Initialize members of the class
        if capture_date is not APIHelper.SKIP:
            self.capture_date = capture_date 
        if invoices is not APIHelper.SKIP:
            self.invoices = invoices 

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
        capture_date = dictionary.get("capture_date") if dictionary.get("capture_date") else APIHelper.SKIP
        invoices = None
        if dictionary.get('invoices') is not None:
            invoices = [InvoiceBalanceItem.from_dictionary(x) for x in dictionary.get('invoices')]
        else:
            invoices = APIHelper.SKIP
        # Return an object of this model
        return cls(capture_date,
                   invoices)
