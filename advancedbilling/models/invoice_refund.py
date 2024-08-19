# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceRefund(object):

    """Implementation of the 'Invoice Refund' model.

    TODO: type model description here.

    Attributes:
        transaction_id (int): TODO: type description here.
        payment_id (int): TODO: type description here.
        memo (str): TODO: type description here.
        original_amount (str): TODO: type description here.
        applied_amount (str): TODO: type description here.
        gateway_transaction_id (str): The transaction ID for the refund as
            returned from the payment gateway
        gateway_used (str): TODO: type description here.
        gateway_handle (str): TODO: type description here.
        ach_late_reject (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transaction_id',
        "payment_id": 'payment_id',
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "gateway_transaction_id": 'gateway_transaction_id',
        "gateway_used": 'gateway_used',
        "gateway_handle": 'gateway_handle',
        "ach_late_reject": 'ach_late_reject'
    }

    _optionals = [
        'transaction_id',
        'payment_id',
        'memo',
        'original_amount',
        'applied_amount',
        'gateway_transaction_id',
        'gateway_used',
        'gateway_handle',
        'ach_late_reject',
    ]

    _nullables = [
        'gateway_transaction_id',
        'gateway_handle',
        'ach_late_reject',
    ]

    def __init__(self,
                 transaction_id=APIHelper.SKIP,
                 payment_id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 gateway_transaction_id=APIHelper.SKIP,
                 gateway_used=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 ach_late_reject=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoiceRefund class"""

        # Initialize members of the class
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if payment_id is not APIHelper.SKIP:
            self.payment_id = payment_id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if gateway_transaction_id is not APIHelper.SKIP:
            self.gateway_transaction_id = gateway_transaction_id 
        if gateway_used is not APIHelper.SKIP:
            self.gateway_used = gateway_used 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if ach_late_reject is not APIHelper.SKIP:
            self.ach_late_reject = ach_late_reject 

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
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        gateway_transaction_id = dictionary.get("gateway_transaction_id") if "gateway_transaction_id" in dictionary.keys() else APIHelper.SKIP
        gateway_used = dictionary.get("gateway_used") if dictionary.get("gateway_used") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        ach_late_reject = dictionary.get("ach_late_reject") if "ach_late_reject" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(transaction_id,
                   payment_id,
                   memo,
                   original_amount,
                   applied_amount,
                   gateway_transaction_id,
                   gateway_used,
                   gateway_handle,
                   ach_late_reject,
                   dictionary)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
