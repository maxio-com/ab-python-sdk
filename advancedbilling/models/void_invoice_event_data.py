# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.credit_note import CreditNote


class VoidInvoiceEventData(object):

    """Implementation of the 'Void Invoice Event Data' model.

    Example schema for an `void_invoice` event

    Attributes:
        credit_note_attributes (CreditNote): The model property of type
            CreditNote.
        memo (str): The memo provided during invoice voiding.
        applied_amount (str): The amount of the void.
        transaction_time (datetime): The time the refund was applied, in ISO
            8601 format, i.e. "2019-06-07T17:20:06Z"
        is_advance_invoice (bool): If true, the invoice is an advance invoice.
        reason (str): The reason for the void.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_note_attributes": 'credit_note_attributes',
        "memo": 'memo',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time',
        "is_advance_invoice": 'is_advance_invoice',
        "reason": 'reason'
    }

    _nullables = [
        'credit_note_attributes',
        'memo',
        'applied_amount',
        'transaction_time',
    ]

    def __init__(self,
                 credit_note_attributes=None,
                 memo=None,
                 applied_amount=None,
                 transaction_time=None,
                 is_advance_invoice=None,
                 reason=None,
                 additional_properties=None):
        """Constructor for the VoidInvoiceEventData class"""

        # Initialize members of the class
        self.credit_note_attributes = credit_note_attributes 
        self.memo = memo 
        self.applied_amount = applied_amount 
        self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        self.is_advance_invoice = is_advance_invoice 
        self.reason = reason 

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
        credit_note_attributes = CreditNote.from_dictionary(dictionary.get('credit_note_attributes')) if dictionary.get('credit_note_attributes') else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else None
        is_advance_invoice = dictionary.get("is_advance_invoice") if "is_advance_invoice" in dictionary.keys() else None
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(credit_note_attributes,
                   memo,
                   applied_amount,
                   transaction_time,
                   is_advance_invoice,
                   reason,
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
            return APIHelper.is_valid_type(value=dictionary.credit_note_attributes,
                                           type_callable=lambda value: CreditNote.validate(value),
                                           is_value_nullable=True,
                                           is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.memo,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount,
                                            type_callable=lambda value: isinstance(value, str),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.transaction_time,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.is_advance_invoice,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.reason,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('credit_note_attributes'),
                                       type_callable=lambda value: CreditNote.validate(value),
                                       is_value_nullable=True,
                                       is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_time'),
                                        type_callable=lambda value: isinstance(value, str),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('is_advance_invoice'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('reason'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'credit_note_attributes={self.credit_note_attributes!r}, '
                f'memo={self.memo!r}, '
                f'applied_amount={self.applied_amount!r}, '
                f'transaction_time={self.transaction_time!r}, '
                f'is_advance_invoice={self.is_advance_invoice!r}, '
                f'reason={self.reason!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'credit_note_attributes={self.credit_note_attributes!s}, '
                f'memo={self.memo!s}, '
                f'applied_amount={self.applied_amount!s}, '
                f'transaction_time={self.transaction_time!s}, '
                f'is_advance_invoice={self.is_advance_invoice!s}, '
                f'reason={self.reason!s}, '
                f'additional_properties={self.additional_properties!s})')
