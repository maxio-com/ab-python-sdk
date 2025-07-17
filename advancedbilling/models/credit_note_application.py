# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreditNoteApplication(object):

    """Implementation of the 'Credit Note Application' model.

    Attributes:
        uid (str): The model property of type str.
        transaction_time (datetime): The model property of type datetime.
        invoice_uid (str): The model property of type str.
        memo (str): The model property of type str.
        applied_amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        invoice_uid = dictionary.get("invoice_uid") if dictionary.get("invoice_uid") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   transaction_time,
                   invoice_uid,
                   memo,
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
                f'transaction_time={(self.transaction_time if hasattr(self, "transaction_time") else None)!r}, '
                f'invoice_uid={(self.invoice_uid if hasattr(self, "invoice_uid") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'transaction_time={(self.transaction_time if hasattr(self, "transaction_time") else None)!s}, '
                f'invoice_uid={(self.invoice_uid if hasattr(self, "invoice_uid") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
