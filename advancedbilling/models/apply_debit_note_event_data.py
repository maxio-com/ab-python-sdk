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

    _optionals = [
        'debit_note_number',
        'debit_note_uid',
        'original_amount',
        'applied_amount',
    ]

    def __init__(self,
                 debit_note_number=APIHelper.SKIP,
                 debit_note_uid=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP):
        """Constructor for the ApplyDebitNoteEventData class"""

        # Initialize members of the class
        if debit_note_number is not APIHelper.SKIP:
            self.debit_note_number = debit_note_number 
        if debit_note_uid is not APIHelper.SKIP:
            self.debit_note_uid = debit_note_uid 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        debit_note_number = dictionary.get("debit_note_number") if dictionary.get("debit_note_number") else APIHelper.SKIP
        debit_note_uid = dictionary.get("debit_note_uid") if dictionary.get("debit_note_uid") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
