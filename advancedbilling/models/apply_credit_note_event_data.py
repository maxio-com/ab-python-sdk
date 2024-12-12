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
        applied_amount (str): The amount of the credit note applied to invoice.
        transaction_time (datetime): The time the credit note was applied, in
            ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
        memo (str): The credit note memo.
        role (str): The role of the credit note (e.g. 'general')
        consolidated_invoice (bool): Shows whether it was applied to
            consolidated invoice or not
        applied_credit_notes (List[AppliedCreditNoteData]): List of credit
            notes applied to children invoices (if consolidated invoice)
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        'transaction_time',
        'memo',
        'role',
        'consolidated_invoice',
        'applied_credit_notes',
    ]

    _nullables = [
        'memo',
    ]

    def __init__(self,
                 uid=None,
                 credit_note_number=None,
                 credit_note_uid=None,
                 original_amount=None,
                 applied_amount=None,
                 transaction_time=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 role=APIHelper.SKIP,
                 consolidated_invoice=APIHelper.SKIP,
                 applied_credit_notes=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ApplyCreditNoteEventData class"""

        # Initialize members of the class
        self.uid = uid 
        self.credit_note_number = credit_note_number 
        self.credit_note_uid = credit_note_uid 
        self.original_amount = original_amount 
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
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        credit_note_number = dictionary.get("credit_note_number") if dictionary.get("credit_note_number") else None
        credit_note_uid = dictionary.get("credit_note_uid") if dictionary.get("credit_note_uid") else None
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        consolidated_invoice = dictionary.get("consolidated_invoice") if "consolidated_invoice" in dictionary.keys() else APIHelper.SKIP
        applied_credit_notes = None
        if dictionary.get('applied_credit_notes') is not None:
            applied_credit_notes = [AppliedCreditNoteData.from_dictionary(x) for x in dictionary.get('applied_credit_notes')]
        else:
            applied_credit_notes = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   applied_credit_notes,
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
            return APIHelper.is_valid_type(value=dictionary.uid,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.credit_note_number,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.credit_note_uid,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.original_amount,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('uid'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('credit_note_number'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('credit_note_uid'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('original_amount'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'),
                                        type_callable=lambda value: isinstance(value, str))
