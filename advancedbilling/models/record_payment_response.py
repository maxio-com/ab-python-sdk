# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.paid_invoice import PaidInvoice


class RecordPaymentResponse(object):

    """Implementation of the 'Record Payment Response' model.

    TODO: type model description here.

    Attributes:
        paid_invoices (List[PaidInvoice]): TODO: type description here.
        prepayment (InvoicePrePayment | None): TODO: type description here.

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
                 additional_properties={}):
        """Constructor for the RecordPaymentResponse class"""

        # Initialize members of the class
        if paid_invoices is not APIHelper.SKIP:
            self.paid_invoices = paid_invoices 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        paid_invoices = None
        if dictionary.get('paid_invoices') is not None:
            paid_invoices = [PaidInvoice.from_dictionary(x) for x in dictionary.get('paid_invoices')]
        else:
            paid_invoices = APIHelper.SKIP
        if 'prepayment' in dictionary.keys():
            prepayment = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RecordPaymentResponsePrepayment'), dictionary.get('prepayment'), False) if dictionary.get('prepayment') is not None else None
        else:
            prepayment = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(paid_invoices,
                   prepayment,
                   dictionary)
