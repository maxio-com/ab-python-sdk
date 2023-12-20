# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateInvoicePaymentApplication(object):

    """Implementation of the 'Create Invoice Payment Application' model.

    TODO: type model description here.

    Attributes:
        invoice_uid (str): Unique identifier for the invoice. It has the
            prefix "inv_" followed by alphanumeric characters.
        amount (str): Dollar amount of the invoice payment (eg. "10.50" =>
            $10.50).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_uid": 'invoice_uid',
        "amount": 'amount'
    }

    def __init__(self,
                 invoice_uid=None,
                 amount=None):
        """Constructor for the CreateInvoicePaymentApplication class"""

        # Initialize members of the class
        self.invoice_uid = invoice_uid 
        self.amount = amount 

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
        invoice_uid = dictionary.get("invoice_uid") if dictionary.get("invoice_uid") else None
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        # Return an object of this model
        return cls(invoice_uid,
                   amount)

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
            return APIHelper.is_valid_type(value=dictionary.invoice_uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.amount, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('invoice_uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('amount'), type_callable=lambda value: isinstance(value, str))
