# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_invoice import CreateInvoice


class CreateInvoiceRequest(object):

    """Implementation of the 'Create Invoice Request' model.

    TODO: type model description here.

    Attributes:
        invoice (CreateInvoice): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice": 'invoice'
    }

    def __init__(self,
                 invoice=None):
        """Constructor for the CreateInvoiceRequest class"""

        # Initialize members of the class
        self.invoice = invoice 

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
        invoice = CreateInvoice.from_dictionary(dictionary.get('invoice')) if dictionary.get('invoice') else None
        # Return an object of this model
        return cls(invoice)
