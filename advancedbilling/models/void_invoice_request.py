# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.void_invoice import VoidInvoice


class VoidInvoiceRequest(object):

    """Implementation of the 'Void Invoice Request' model.

    TODO: type model description here.

    Attributes:
        void (VoidInvoice): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "void": 'void'
    }

    def __init__(self,
                 void=None):
        """Constructor for the VoidInvoiceRequest class"""

        # Initialize members of the class
        self.void = void 

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
        void = VoidInvoice.from_dictionary(dictionary.get('void')) if dictionary.get('void') else None
        # Return an object of this model
        return cls(void)
