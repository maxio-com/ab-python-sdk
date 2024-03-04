# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePaymentApplication(object):

    """Implementation of the 'Invoice Payment Application' model.

    TODO: type model description here.

    Attributes:
        invoice_uid (str): Unique identifier for the paid invoice. It has the
            prefix "inv_" followed by alphanumeric characters.
        application_uid (str): Unique identifier for the payment. It has the
            prefix "pmt_" followed by alphanumeric characters.
        applied_amount (str): Dollar amount of the paid invoice.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_uid": 'invoice_uid',
        "application_uid": 'application_uid',
        "applied_amount": 'applied_amount'
    }

    _optionals = [
        'invoice_uid',
        'application_uid',
        'applied_amount',
    ]

    def __init__(self,
                 invoice_uid=APIHelper.SKIP,
                 application_uid=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoicePaymentApplication class"""

        # Initialize members of the class
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid 
        if application_uid is not APIHelper.SKIP:
            self.application_uid = application_uid 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 

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
        invoice_uid = dictionary.get("invoice_uid") if dictionary.get("invoice_uid") else APIHelper.SKIP
        application_uid = dictionary.get("application_uid") if dictionary.get("application_uid") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(invoice_uid,
                   application_uid,
                   applied_amount,
                   dictionary)
