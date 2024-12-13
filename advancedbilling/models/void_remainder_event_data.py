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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_note_attributes": 'credit_note_attributes',
        "memo": 'memo',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time'
    }

    def __init__(self,
                 credit_note_attributes=None,
                 memo=None,
                 applied_amount=None,
                 transaction_time=None,
                 additional_properties=None):
        """Constructor for the VoidRemainderEventData class"""

        # Initialize members of the class
        self.credit_note_attributes = credit_note_attributes 
        self.memo = memo 
        self.applied_amount = applied_amount 
        self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 

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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(credit_note_attributes,
                   memo,
                   applied_amount,
                   transaction_time,
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
                                           is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.memo,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.transaction_time,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('credit_note_attributes'),
                                       type_callable=lambda value: CreditNote.validate(value),
                                       is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_time'),
                                        type_callable=lambda value: isinstance(value, str))
