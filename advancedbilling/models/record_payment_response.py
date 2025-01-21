# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_pre_payment import InvoicePrePayment
from advancedbilling.models.paid_invoice import PaidInvoice


class RecordPaymentResponse(object):

    """Implementation of the 'Record Payment Response' model.

    Attributes:
        paid_invoices (List[PaidInvoice]): The model property of type
            List[PaidInvoice].
        prepayment (InvoicePrePayment): The model property of type
            InvoicePrePayment.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "paid_invoices": 'paid_invoices',
        "prepayment": 'prepayment'
    }

    _optionals = [
        'paid_invoices',
        'prepayment',
    ]

    _nullables = [
        'prepayment',
    ]

    def __init__(self,
                 paid_invoices=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RecordPaymentResponse class"""

        # Initialize members of the class
        if paid_invoices is not APIHelper.SKIP:
            self.paid_invoices = paid_invoices 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 

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
        paid_invoices = None
        if dictionary.get('paid_invoices') is not None:
            paid_invoices = [PaidInvoice.from_dictionary(x) for x in dictionary.get('paid_invoices')]
        else:
            paid_invoices = APIHelper.SKIP
        if 'prepayment' in dictionary.keys():
            prepayment = InvoicePrePayment.from_dictionary(dictionary.get('prepayment')) if dictionary.get('prepayment') else None
        else:
            prepayment = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(paid_invoices,
                   prepayment,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'paid_invoices={self.paid_invoices!r}, '
                f'prepayment={self.prepayment!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'paid_invoices={self.paid_invoices!s}, '
                f'prepayment={self.prepayment!s}, '
                f'additional_properties={self.additional_properties!s})')
