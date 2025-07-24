# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ServiceCredit1(object):

    """Implementation of the 'Service Credit1' model.

    Attributes:
        id (int): The model property of type int.
        amount_in_cents (int): The amount in cents of the entry
        ending_balance_in_cents (int): The new balance for the credit account
        entry_type (ServiceCreditType): The type of entry
        memo (str): The memo attached to the entry
        invoice_uid (str): The invoice uid associated with the entry. Only
            present for debit entries
        remaining_balance_in_cents (int): The remaining balance for the entry
        created_at (datetime): The date and time the entry was created
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "amount_in_cents": 'amount_in_cents',
        "ending_balance_in_cents": 'ending_balance_in_cents',
        "entry_type": 'entry_type',
        "memo": 'memo',
        "invoice_uid": 'invoice_uid',
        "remaining_balance_in_cents": 'remaining_balance_in_cents',
        "created_at": 'created_at'
    }

    _optionals = [
        'id',
        'amount_in_cents',
        'ending_balance_in_cents',
        'entry_type',
        'memo',
        'invoice_uid',
        'remaining_balance_in_cents',
        'created_at',
    ]

    _nullables = [
        'invoice_uid',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 ending_balance_in_cents=APIHelper.SKIP,
                 entry_type=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 invoice_uid=APIHelper.SKIP,
                 remaining_balance_in_cents=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ServiceCredit1 class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if ending_balance_in_cents is not APIHelper.SKIP:
            self.ending_balance_in_cents = ending_balance_in_cents 
        if entry_type is not APIHelper.SKIP:
            self.entry_type = entry_type 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid 
        if remaining_balance_in_cents is not APIHelper.SKIP:
            self.remaining_balance_in_cents = remaining_balance_in_cents 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        ending_balance_in_cents = dictionary.get("ending_balance_in_cents") if dictionary.get("ending_balance_in_cents") else APIHelper.SKIP
        entry_type = dictionary.get("entry_type") if dictionary.get("entry_type") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        invoice_uid = dictionary.get("invoice_uid") if "invoice_uid" in dictionary.keys() else APIHelper.SKIP
        remaining_balance_in_cents = dictionary.get("remaining_balance_in_cents") if dictionary.get("remaining_balance_in_cents") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   amount_in_cents,
                   ending_balance_in_cents,
                   entry_type,
                   memo,
                   invoice_uid,
                   remaining_balance_in_cents,
                   created_at,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'ending_balance_in_cents={(self.ending_balance_in_cents if hasattr(self, "ending_balance_in_cents") else None)!r}, '
                f'entry_type={(self.entry_type if hasattr(self, "entry_type") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'invoice_uid={(self.invoice_uid if hasattr(self, "invoice_uid") else None)!r}, '
                f'remaining_balance_in_cents={(self.remaining_balance_in_cents if hasattr(self, "remaining_balance_in_cents") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'ending_balance_in_cents={(self.ending_balance_in_cents if hasattr(self, "ending_balance_in_cents") else None)!s}, '
                f'entry_type={(self.entry_type if hasattr(self, "entry_type") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'invoice_uid={(self.invoice_uid if hasattr(self, "invoice_uid") else None)!s}, '
                f'remaining_balance_in_cents={(self.remaining_balance_in_cents if hasattr(self, "remaining_balance_in_cents") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
