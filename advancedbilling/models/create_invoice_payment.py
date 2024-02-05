# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateInvoicePayment(object):

    """Implementation of the 'Create Invoice Payment' model.

    TODO: type model description here.

    Attributes:
        amount (str | float | None): A string of the dollar amount to be
            refunded (eg. "10.50" => $10.50)
        memo (str): A description to be attached to the payment.
        method (InvoicePaymentMethodType): The type of payment method used.
            Defaults to other.
        details (str): Additional information related to the payment method
            (eg. Check #)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo',
        "method": 'method',
        "details": 'details'
    }

    _optionals = [
        'amount',
        'memo',
        'method',
        'details',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 method=APIHelper.SKIP,
                 details=APIHelper.SKIP):
        """Constructor for the CreateInvoicePayment class"""

        # Initialize members of the class
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if method is not APIHelper.SKIP:
            self.method = method 
        if details is not APIHelper.SKIP:
            self.details = details 

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
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoicePaymentAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        method = dictionary.get("method") if dictionary.get("method") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   memo,
                   method,
                   details)
