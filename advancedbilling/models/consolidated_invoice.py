# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice import Invoice


class ConsolidatedInvoice(object):

    """Implementation of the 'Consolidated Invoice' model.

    TODO: type model description here.

    Attributes:
        invoices (List[Invoice]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoices": 'invoices'
    }

    _optionals = [
        'invoices',
    ]

    def __init__(self,
                 invoices=APIHelper.SKIP):
        """Constructor for the ConsolidatedInvoice class"""

        # Initialize members of the class
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
        invoices = None
        if dictionary.get('invoices') is not None:
            invoices = [Invoice.from_dictionary(x) for x in dictionary.get('invoices')]
        else:
            invoices = APIHelper.SKIP
        # Return an object of this model
        return cls(invoices)
