# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.proforma_invoice import ProformaInvoice


class SignupProformaPreview(object):

    """Implementation of the 'Signup Proforma Preview' model.

    TODO: type model description here.

    Attributes:
        current_proforma_invoice (ProformaInvoice): TODO: type description
            here.
        next_proforma_invoice (ProformaInvoice): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_proforma_invoice": 'current_proforma_invoice',
        "next_proforma_invoice": 'next_proforma_invoice'
    }

    _optionals = [
        'current_proforma_invoice',
        'next_proforma_invoice',
    ]

    def __init__(self,
                 current_proforma_invoice=APIHelper.SKIP,
                 next_proforma_invoice=APIHelper.SKIP):
        """Constructor for the SignupProformaPreview class"""

        # Initialize members of the class
        if current_proforma_invoice is not APIHelper.SKIP:
            self.current_proforma_invoice = current_proforma_invoice 
        if next_proforma_invoice is not APIHelper.SKIP:
            self.next_proforma_invoice = next_proforma_invoice 

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
        current_proforma_invoice = ProformaInvoice.from_dictionary(dictionary.get('current_proforma_invoice')) if 'current_proforma_invoice' in dictionary.keys() else APIHelper.SKIP
        next_proforma_invoice = ProformaInvoice.from_dictionary(dictionary.get('next_proforma_invoice')) if 'next_proforma_invoice' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(current_proforma_invoice,
                   next_proforma_invoice)
