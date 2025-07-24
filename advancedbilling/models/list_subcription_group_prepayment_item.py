# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListSubcriptionGroupPrepaymentItem(object):

    """Implementation of the 'List Subcription Group Prepayment Item' model.

    Attributes:
        id (int): The model property of type int.
        subscription_group_uid (str): The model property of type str.
        amount_in_cents (int): The model property of type int.
        remaining_amount_in_cents (int): The model property of type int.
        details (str): The model property of type str.
        external (bool): The model property of type bool.
        memo (str): The model property of type str.
        payment_type (PrepaymentMethod): The model property of type
            PrepaymentMethod.
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "subscription_group_uid": 'subscription_group_uid',
        "amount_in_cents": 'amount_in_cents',
        "remaining_amount_in_cents": 'remaining_amount_in_cents',
        "details": 'details',
        "external": 'external',
        "memo": 'memo',
        "payment_type": 'payment_type',
        "created_at": 'created_at'
    }

    _optionals = [
        'id',
        'subscription_group_uid',
        'amount_in_cents',
        'remaining_amount_in_cents',
        'details',
        'external',
        'memo',
        'payment_type',
        'created_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 subscription_group_uid=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 remaining_amount_in_cents=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 external=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListSubcriptionGroupPrepaymentItem class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if subscription_group_uid is not APIHelper.SKIP:
            self.subscription_group_uid = subscription_group_uid 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if remaining_amount_in_cents is not APIHelper.SKIP:
            self.remaining_amount_in_cents = remaining_amount_in_cents 
        if details is not APIHelper.SKIP:
            self.details = details 
        if external is not APIHelper.SKIP:
            self.external = external 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
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
        subscription_group_uid = dictionary.get("subscription_group_uid") if dictionary.get("subscription_group_uid") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        remaining_amount_in_cents = dictionary.get("remaining_amount_in_cents") if dictionary.get("remaining_amount_in_cents") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   subscription_group_uid,
                   amount_in_cents,
                   remaining_amount_in_cents,
                   details,
                   external,
                   memo,
                   payment_type,
                   created_at,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'subscription_group_uid={(self.subscription_group_uid if hasattr(self, "subscription_group_uid") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'remaining_amount_in_cents={(self.remaining_amount_in_cents if hasattr(self, "remaining_amount_in_cents") else None)!r}, '
                f'details={(self.details if hasattr(self, "details") else None)!r}, '
                f'external={(self.external if hasattr(self, "external") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'payment_type={(self.payment_type if hasattr(self, "payment_type") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'subscription_group_uid={(self.subscription_group_uid if hasattr(self, "subscription_group_uid") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'remaining_amount_in_cents={(self.remaining_amount_in_cents if hasattr(self, "remaining_amount_in_cents") else None)!s}, '
                f'details={(self.details if hasattr(self, "details") else None)!s}, '
                f'external={(self.external if hasattr(self, "external") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'payment_type={(self.payment_type if hasattr(self, "payment_type") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
