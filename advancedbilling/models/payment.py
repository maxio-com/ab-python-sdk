# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Payment(object):

    """Implementation of the 'Payment' model.

    TODO: type model description here.

    Attributes:
        invoice_uid (str): The uid of the paid invoice
        status (Status): The current status of the invoice. See [Invoice
            Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494
            171#line-item-breakdowns) for more.
        due_amount (str): The remaining due amount on the invoice
        paid_amount (str): The total amount paid on this invoice (including
            any prior payments)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_uid": 'invoice_uid',
        "status": 'status',
        "due_amount": 'due_amount',
        "paid_amount": 'paid_amount'
    }

    _optionals = [
        'invoice_uid',
        'status',
        'due_amount',
        'paid_amount',
    ]

    def __init__(self,
                 invoice_uid=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 due_amount=APIHelper.SKIP,
                 paid_amount=APIHelper.SKIP):
        """Constructor for the Payment class"""

        # Initialize members of the class
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid 
        if status is not APIHelper.SKIP:
            self.status = status 
        if due_amount is not APIHelper.SKIP:
            self.due_amount = due_amount 
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount 

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
        invoice_uid = dictionary.get("invoice_uid") if dictionary.get("invoice_uid") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(invoice_uid,
                   status,
                   due_amount,
                   paid_amount)
