# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_payment_application import InvoicePaymentApplication


class MultiInvoicePayment(object):

    """Implementation of the 'Multi Invoice Payment' model.

    Attributes:
        transaction_id (int): The numeric ID of the transaction.
        total_amount (str): Dollar amount of the sum of the paid invoices.
        currency_code (str): The ISO 4217 currency code (3 character string)
            representing the currency of invoice transaction.
        applications (List[InvoicePaymentApplication]): The model property of
            type List[InvoicePaymentApplication].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transaction_id',
        "total_amount": 'total_amount',
        "currency_code": 'currency_code',
        "applications": 'applications'
    }

    _optionals = [
        'transaction_id',
        'total_amount',
        'currency_code',
        'applications',
    ]

    def __init__(self,
                 transaction_id=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP,
                 currency_code=APIHelper.SKIP,
                 applications=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the MultiInvoicePayment class"""

        # Initialize members of the class
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if total_amount is not APIHelper.SKIP:
            self.total_amount = total_amount 
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code 
        if applications is not APIHelper.SKIP:
            self.applications = applications 

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
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        currency_code = dictionary.get("currency_code") if dictionary.get("currency_code") else APIHelper.SKIP
        applications = None
        if dictionary.get('applications') is not None:
            applications = [InvoicePaymentApplication.from_dictionary(x) for x in dictionary.get('applications')]
        else:
            applications = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(transaction_id,
                   total_amount,
                   currency_code,
                   applications,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!r}, '
                f'total_amount={(self.total_amount if hasattr(self, "total_amount") else None)!r}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!r}, '
                f'applications={(self.applications if hasattr(self, "applications") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!s}, '
                f'total_amount={(self.total_amount if hasattr(self, "total_amount") else None)!s}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!s}, '
                f'applications={(self.applications if hasattr(self, "applications") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
