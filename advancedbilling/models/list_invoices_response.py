# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.invoice import Invoice


class ListInvoicesResponse(object):

    """Implementation of the 'List Invoices Response' model.

    TODO: type model description here.

    Attributes:
        invoices (List[Invoice]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoices": 'invoices'
    }

    def __init__(self,
                 invoices=None,
                 additional_properties={}):
        """Constructor for the ListInvoicesResponse class"""

        # Initialize members of the class
        self.invoices = invoices 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

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
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(invoices,
                   dictionary)
