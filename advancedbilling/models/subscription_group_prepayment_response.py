# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupPrepaymentResponse(object):

    """Implementation of the 'Subscription Group Prepayment Response' model.

    Attributes:
        id (int): The model property of type int.
        amount_in_cents (int): The amount in cents of the entry.
        ending_balance_in_cents (int): The ending balance in cents of the
            account.
        entry_type (ServiceCreditType): The type of entry
        memo (str): A memo attached to the entry.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "amount_in_cents": 'amount_in_cents',
        "ending_balance_in_cents": 'ending_balance_in_cents',
        "entry_type": 'entry_type',
        "memo": 'memo'
    }

    _optionals = [
        'id',
        'amount_in_cents',
        'ending_balance_in_cents',
        'entry_type',
        'memo',
    ]

    _nullables = [
        'memo',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 ending_balance_in_cents=APIHelper.SKIP,
                 entry_type=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupPrepaymentResponse class"""

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
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   amount_in_cents,
                   ending_balance_in_cents,
                   entry_type,
                   memo,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'ending_balance_in_cents={(self.ending_balance_in_cents if hasattr(self, "ending_balance_in_cents") else None)!r}, '
                f'entry_type={(self.entry_type if hasattr(self, "entry_type") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'ending_balance_in_cents={(self.ending_balance_in_cents if hasattr(self, "ending_balance_in_cents") else None)!s}, '
                f'entry_type={(self.entry_type if hasattr(self, "entry_type") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
