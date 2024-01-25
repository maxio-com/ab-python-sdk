# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.credit_note import CreditNote


class VoidRemainderEventData(object):

    """Implementation of the 'Void Remainder Event Data' model.

    Example schema for an `void_remainder` event

    Attributes:
        credit_note_attributes (CreditNote): TODO: type description here.
        memo (str): The memo provided during invoice remainder voiding.
        applied_amount (str): The amount of the void.
        transaction_time (datetime): The time the refund was applied, in ISO
            8601 format, i.e. "2019-06-07T17:20:06Z"

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_note_attributes": 'credit_note_attributes',
        "memo": 'memo',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time'
    }

    _optionals = [
        'credit_note_attributes',
        'memo',
        'applied_amount',
        'transaction_time',
    ]

    def __init__(self,
                 credit_note_attributes=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP):
        """Constructor for the VoidRemainderEventData class"""

        # Initialize members of the class
        if credit_note_attributes is not APIHelper.SKIP:
            self.credit_note_attributes = credit_note_attributes 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 

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
        credit_note_attributes = CreditNote.from_dictionary(dictionary.get('credit_note_attributes')) if 'credit_note_attributes' in dictionary.keys() else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        # Return an object of this model
        return cls(credit_note_attributes,
                   memo,
                   applied_amount,
                   transaction_time)

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
