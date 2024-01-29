# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_pre_payment import InvoicePrePayment
from advancedbilling.models.payment import Payment


class PaymentResponse(object):

    """Implementation of the 'Payment Response' model.

    TODO: type model description here.

    Attributes:
        paid_invoices (List[Payment]): TODO: type description here.
        prepayment (InvoicePrePayment): TODO: type description here.

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

    def __init__(self,
                 paid_invoices=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP):
        """Constructor for the PaymentResponse class"""

        # Initialize members of the class
        if paid_invoices is not APIHelper.SKIP:
            self.paid_invoices = paid_invoices 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 

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
        paid_invoices = None
        if dictionary.get('paid_invoices') is not None:
            paid_invoices = [Payment.from_dictionary(x) for x in dictionary.get('paid_invoices')]
        else:
            paid_invoices = APIHelper.SKIP
        prepayment = InvoicePrePayment.from_dictionary(dictionary.get('prepayment')) if 'prepayment' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(paid_invoices,
                   prepayment)
