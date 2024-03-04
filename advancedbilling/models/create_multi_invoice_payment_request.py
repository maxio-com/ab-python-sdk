# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_multi_invoice_payment import CreateMultiInvoicePayment


class CreateMultiInvoicePaymentRequest(object):

    """Implementation of the 'Create Multi Invoice Payment Request' model.

    TODO: type model description here.

    Attributes:
        payment (CreateMultiInvoicePayment): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment'
    }

    def __init__(self,
                 payment=None,
                 additional_properties={}):
        """Constructor for the CreateMultiInvoicePaymentRequest class"""

        # Initialize members of the class
        self.payment = payment 

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
        payment = CreateMultiInvoicePayment.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(payment,
                   dictionary)
