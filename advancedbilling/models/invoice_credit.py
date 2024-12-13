# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceCredit(object):

    """Implementation of the 'Invoice Credit' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        credit_note_number (str): TODO: type description here.
        credit_note_uid (str): TODO: type description here.
        transaction_time (datetime): TODO: type description here.
        memo (str): TODO: type description here.
        original_amount (str): TODO: type description here.
        applied_amount (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "credit_note_number": 'credit_note_number',
        "credit_note_uid": 'credit_note_uid',
        "transaction_time": 'transaction_time',
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount'
    }

    _optionals = [
        'uid',
        'credit_note_number',
        'credit_note_uid',
        'transaction_time',
        'memo',
        'original_amount',
        'applied_amount',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 credit_note_number=APIHelper.SKIP,
                 credit_note_uid=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceCredit class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if credit_note_number is not APIHelper.SKIP:
            self.credit_note_number = credit_note_number 
        if credit_note_uid is not APIHelper.SKIP:
            self.credit_note_uid = credit_note_uid 
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        credit_note_number = dictionary.get("credit_note_number") if dictionary.get("credit_note_number") else APIHelper.SKIP
        credit_note_uid = dictionary.get("credit_note_uid") if dictionary.get("credit_note_uid") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   credit_note_number,
                   credit_note_uid,
                   transaction_time,
                   memo,
                   original_amount,
                   applied_amount,
                   additional_properties)

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
