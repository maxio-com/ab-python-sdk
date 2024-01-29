# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ApplyDebitNoteEventData(object):

    """Implementation of the 'Apply Debit Note Event Data' model.

    Example schema for an `apply_debit_note` event

    Attributes:
        debit_note_number (str): A unique, identifying string that appears on
            the debit note and in places it is referenced.
        debit_note_uid (str): Unique identifier for the debit note. It is
            generated automatically by Chargify and has the prefix "db_"
            followed by alphanumeric characters.
        original_amount (str): The full, original amount of the debit note.
        applied_amount (str): The amount of the debit note applied to
            invoice.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "debit_note_number": 'debit_note_number',
        "debit_note_uid": 'debit_note_uid',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount'
    }

    def __init__(self,
                 debit_note_number=None,
                 debit_note_uid=None,
                 original_amount=None,
                 applied_amount=None):
        """Constructor for the ApplyDebitNoteEventData class"""

        # Initialize members of the class
        self.debit_note_number = debit_note_number 
        self.debit_note_uid = debit_note_uid 
        self.original_amount = original_amount 
        self.applied_amount = applied_amount 

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
        debit_note_number = dictionary.get("debit_note_number") if dictionary.get("debit_note_number") else None
        debit_note_uid = dictionary.get("debit_note_uid") if dictionary.get("debit_note_uid") else None
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        # Return an object of this model
        return cls(debit_note_number,
                   debit_note_uid,
                   original_amount,
                   applied_amount)

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
            return APIHelper.is_valid_type(value=dictionary.debit_note_number, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.debit_note_uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.original_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('debit_note_number'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('debit_note_uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('original_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'), type_callable=lambda value: isinstance(value, str))
