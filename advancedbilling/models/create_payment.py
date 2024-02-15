# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreatePayment(object):

    """Implementation of the 'Create Payment' model.

    TODO: type model description here.

    Attributes:
        amount (str): TODO: type description here.
        memo (str): TODO: type description here.
        payment_details (str): TODO: type description here.
        payment_method (InvoicePaymentMethodType): The type of payment method
            used. Defaults to other.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo',
        "payment_details": 'payment_details',
        "payment_method": 'payment_method'
    }

    def __init__(self,
                 amount=None,
                 memo=None,
                 payment_details=None,
                 payment_method=None):
        """Constructor for the CreatePayment class"""

        # Initialize members of the class
        self.amount = amount 
        self.memo = memo 
        self.payment_details = payment_details 
        self.payment_method = payment_method 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        payment_details = dictionary.get("payment_details") if dictionary.get("payment_details") else None
        payment_method = dictionary.get("payment_method") if dictionary.get("payment_method") else None
        # Return an object of this model
        return cls(amount,
                   memo,
                   payment_details,
                   payment_method)
