# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_invoice_payment import CreateInvoicePayment


class CreateInvoicePaymentRequest(object):

    """Implementation of the 'Create Invoice Payment Request' model.

    TODO: type model description here.

    Attributes:
        payment (CreateInvoicePayment): TODO: type description here.
        mtype (InvoicePaymentType): The type of payment to be applied to an
            Invoice. Defaults to external.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment',
        "mtype": 'type'
    }

    _optionals = [
        'mtype',
    ]

    def __init__(self,
                 payment=None,
                 mtype=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreateInvoicePaymentRequest class"""

        # Initialize members of the class
        self.payment = payment 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

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
        payment = CreateInvoicePayment.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(payment,
                   mtype,
                   dictionary)
