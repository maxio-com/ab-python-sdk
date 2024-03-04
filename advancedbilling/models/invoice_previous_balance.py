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
        captured_at (datetime): TODO: type description here.
        invoices (List[InvoiceBalanceItem]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "captured_at": 'captured_at',
        "invoices": 'invoices'
    }

    _optionals = [
        'captured_at',
        'invoices',
    ]

    def __init__(self,
                 captured_at=APIHelper.SKIP,
                 invoices=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoicePreviousBalance class"""

        # Initialize members of the class
        if captured_at is not APIHelper.SKIP:
            self.captured_at = APIHelper.apply_datetime_converter(captured_at, APIHelper.RFC3339DateTime) if captured_at else None 
        if invoices is not APIHelper.SKIP:
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
        captured_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("captured_at")).datetime if dictionary.get("captured_at") else APIHelper.SKIP
        invoices = None
        if dictionary.get('invoices') is not None:
            invoices = [InvoiceBalanceItem.from_dictionary(x) for x in dictionary.get('invoices')]
        else:
            invoices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(captured_at,
                   invoices,
                   dictionary)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
