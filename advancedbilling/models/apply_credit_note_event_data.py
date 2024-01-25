# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.applied_credit_note_data import AppliedCreditNoteData


class ApplyCreditNoteEventData(object):

    """Implementation of the 'Apply Credit Note Event Data' model.

    Example schema for an `apply_credit_note` event

    Attributes:
        uid (str): Unique identifier for the credit note application. It is
            generated automatically by Chargify and has the prefix "cdt_"
            followed by alphanumeric characters.
        credit_note_number (str): A unique, identifying string that appears on
            the credit note and in places it is referenced.
        credit_note_uid (str): Unique identifier for the credit note. It is
            generated automatically by Chargify and has the prefix "cn_"
            followed by alphanumeric characters.
        original_amount (str): The full, original amount of the credit note.
        applied_amount (str): The amount of the credit note applied to
            invoice.
        transaction_time (datetime): The time the credit note was applied, in
            ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
        memo (str): The credit note memo.
        role (str): The role of the credit note (e.g. 'general')
        consolidated_invoice (bool): Shows whether it was applied to
            consolidated invoice or not
        applied_credit_notes (List[AppliedCreditNoteData]): List of credit
            notes applied to children invoices (if consolidated invoice)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "credit_note_number": 'credit_note_number',
        "credit_note_uid": 'credit_note_uid',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time',
        "memo": 'memo',
        "role": 'role',
        "consolidated_invoice": 'consolidated_invoice',
        "applied_credit_notes": 'applied_credit_notes'
    }

    _optionals = [
        'uid',
        'credit_note_number',
        'credit_note_uid',
        'original_amount',
        'applied_amount',
        'transaction_time',
        'memo',
        'role',
        'consolidated_invoice',
        'applied_credit_notes',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 credit_note_number=APIHelper.SKIP,
                 credit_note_uid=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 role=APIHelper.SKIP,
                 consolidated_invoice=APIHelper.SKIP,
                 applied_credit_notes=APIHelper.SKIP):
        """Constructor for the ApplyCreditNoteEventData class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if credit_note_number is not APIHelper.SKIP:
            self.credit_note_number = credit_note_number 
        if credit_note_uid is not APIHelper.SKIP:
            self.credit_note_uid = credit_note_uid 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if role is not APIHelper.SKIP:
            self.role = role 
        if consolidated_invoice is not APIHelper.SKIP:
            self.consolidated_invoice = consolidated_invoice 
        if applied_credit_notes is not APIHelper.SKIP:
            self.applied_credit_notes = applied_credit_notes 

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
        credit_note_number = dictionary.get("credit_note_number") if dictionary.get("credit_note_number") else APIHelper.SKIP
        credit_note_uid = dictionary.get("credit_note_uid") if dictionary.get("credit_note_uid") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        consolidated_invoice = dictionary.get("consolidated_invoice") if "consolidated_invoice" in dictionary.keys() else APIHelper.SKIP
        applied_credit_notes = None
        if dictionary.get('applied_credit_notes') is not None:
            applied_credit_notes = [AppliedCreditNoteData.from_dictionary(x) for x in dictionary.get('applied_credit_notes')]
        else:
            applied_credit_notes = APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   credit_note_number,
                   credit_note_uid,
                   original_amount,
                   applied_amount,
                   transaction_time,
                   memo,
                   role,
                   consolidated_invoice,
                   applied_credit_notes)

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
