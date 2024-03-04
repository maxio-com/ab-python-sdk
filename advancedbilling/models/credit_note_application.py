# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreditNoteApplication(object):

    """Implementation of the 'Credit Note Application' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        transaction_time (datetime): TODO: type description here.
        invoice_uid (str): TODO: type description here.
        memo (str): TODO: type description here.
        applied_amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "transaction_time": 'transaction_time',
        "invoice_uid": 'invoice_uid',
        "memo": 'memo',
        "applied_amount": 'applied_amount'
    }

    _optionals = [
        'uid',
        'transaction_time',
        'invoice_uid',
        'memo',
        'applied_amount',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP,
                 invoice_uid=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreditNoteApplication class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        invoice_uid = dictionary.get("invoice_uid") if dictionary.get("invoice_uid") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(uid,
                   transaction_time,
                   invoice_uid,
                   memo,
                   applied_amount,
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
