# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaidInvoice(object):

    """Implementation of the 'Paid Invoice' model.

    TODO: type model description here.

    Attributes:
        invoice_id (str): The uid of the paid invoice
        status (InvoiceStatus): The current status of the invoice. See
            [Invoice
            Statuses](https://maxio.zendesk.com/hc/en-us/articles/2425228782964
            5-Advanced-Billing-Invoices-Overview#invoice-statuses) for more.
        due_amount (str): The remaining due amount on the invoice
        paid_amount (str): The total amount paid on this invoice (including
            any prior payments)
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_id": 'invoice_id',
        "status": 'status',
        "due_amount": 'due_amount',
        "paid_amount": 'paid_amount'
    }

    _optionals = [
        'invoice_id',
        'status',
        'due_amount',
        'paid_amount',
    ]

    def __init__(self,
                 invoice_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 due_amount=APIHelper.SKIP,
                 paid_amount=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PaidInvoice class"""

        # Initialize members of the class
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if due_amount is not APIHelper.SKIP:
            self.due_amount = due_amount 
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount 

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
        invoice_id = dictionary.get("invoice_id") if dictionary.get("invoice_id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(invoice_id,
                   status,
                   due_amount,
                   paid_amount,
                   additional_properties)
