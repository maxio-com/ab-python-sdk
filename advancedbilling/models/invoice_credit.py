# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceCredit(object):

    """Implementation of the 'Invoice Credit' model.

    Attributes:
        uid (str): The model property of type str.
        credit_note_number (str): The model property of type str.
        credit_note_uid (str): The model property of type str.
        transaction_time (datetime): The model property of type datetime.
        memo (str): The model property of type str.
        original_amount (str): The model property of type str.
        applied_amount (str): The model property of type str.
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'credit_note_number={(self.credit_note_number if hasattr(self, "credit_note_number") else None)!r}, '
                f'credit_note_uid={(self.credit_note_uid if hasattr(self, "credit_note_uid") else None)!r}, '
                f'transaction_time={(self.transaction_time if hasattr(self, "transaction_time") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'original_amount={(self.original_amount if hasattr(self, "original_amount") else None)!r}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'credit_note_number={(self.credit_note_number if hasattr(self, "credit_note_number") else None)!s}, '
                f'credit_note_uid={(self.credit_note_uid if hasattr(self, "credit_note_uid") else None)!s}, '
                f'transaction_time={(self.transaction_time if hasattr(self, "transaction_time") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'original_amount={(self.original_amount if hasattr(self, "original_amount") else None)!s}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
