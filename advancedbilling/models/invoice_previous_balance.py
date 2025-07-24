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

    Attributes:
        captured_at (datetime): The model property of type datetime.
        invoices (List[InvoiceBalanceItem]): The model property of type
            List[InvoiceBalanceItem].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the InvoicePreviousBalance class"""

        # Initialize members of the class
        if captured_at is not APIHelper.SKIP:
            self.captured_at = APIHelper.apply_datetime_converter(captured_at, APIHelper.RFC3339DateTime) if captured_at else None 
        if invoices is not APIHelper.SKIP:
            self.invoices = invoices 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        captured_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("captured_at")).datetime if dictionary.get("captured_at") else APIHelper.SKIP
        invoices = None
        if dictionary.get('invoices') is not None:
            invoices = [InvoiceBalanceItem.from_dictionary(x) for x in dictionary.get('invoices')]
        else:
            invoices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(captured_at,
                   invoices,
                   additional_properties)

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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'captured_at={(self.captured_at if hasattr(self, "captured_at") else None)!r}, '
                f'invoices={(self.invoices if hasattr(self, "invoices") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'captured_at={(self.captured_at if hasattr(self, "captured_at") else None)!s}, '
                f'invoices={(self.invoices if hasattr(self, "invoices") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
