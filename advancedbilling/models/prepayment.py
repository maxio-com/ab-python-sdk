# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Prepayment(object):

    """Implementation of the 'Prepayment' model.

    Attributes:
        id (int): The model property of type int.
        subscription_id (int): The model property of type int.
        amount_in_cents (int): The model property of type int.
        remaining_amount_in_cents (int): The model property of type int.
        refunded_amount_in_cents (int): The model property of type int.
        details (str): The model property of type str.
        external (bool): The model property of type bool.
        memo (str): The model property of type str.
        payment_type (PrepaymentMethod): The payment type of the prepayment.
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "subscription_id": 'subscription_id',
        "amount_in_cents": 'amount_in_cents',
        "remaining_amount_in_cents": 'remaining_amount_in_cents',
        "external": 'external',
        "memo": 'memo',
        "created_at": 'created_at',
        "refunded_amount_in_cents": 'refunded_amount_in_cents',
        "details": 'details',
        "payment_type": 'payment_type'
    }

    _optionals = [
        'refunded_amount_in_cents',
        'details',
        'payment_type',
    ]

    def __init__(self,
                 id=None,
                 subscription_id=None,
                 amount_in_cents=None,
                 remaining_amount_in_cents=None,
                 external=None,
                 memo=None,
                 created_at=None,
                 refunded_amount_in_cents=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Prepayment class"""

        # Initialize members of the class
        self.id = id 
        self.subscription_id = subscription_id 
        self.amount_in_cents = amount_in_cents 
        self.remaining_amount_in_cents = remaining_amount_in_cents 
        if refunded_amount_in_cents is not APIHelper.SKIP:
            self.refunded_amount_in_cents = refunded_amount_in_cents 
        if details is not APIHelper.SKIP:
            self.details = details 
        self.external = external 
        self.memo = memo 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
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
        id = dictionary.get("id") if dictionary.get("id") else None
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        remaining_amount_in_cents = dictionary.get("remaining_amount_in_cents") if dictionary.get("remaining_amount_in_cents") else None
        external = dictionary.get("external") if "external" in dictionary.keys() else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        refunded_amount_in_cents = dictionary.get("refunded_amount_in_cents") if dictionary.get("refunded_amount_in_cents") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   subscription_id,
                   amount_in_cents,
                   remaining_amount_in_cents,
                   external,
                   memo,
                   created_at,
                   refunded_amount_in_cents,
                   details,
                   payment_type,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'subscription_id={self.subscription_id!r}, '
                f'amount_in_cents={self.amount_in_cents!r}, '
                f'remaining_amount_in_cents={self.remaining_amount_in_cents!r}, '
                f'refunded_amount_in_cents={(self.refunded_amount_in_cents if hasattr(self, "refunded_amount_in_cents") else None)!r}, '
                f'details={(self.details if hasattr(self, "details") else None)!r}, '
                f'external={self.external!r}, '
                f'memo={self.memo!r}, '
                f'payment_type={(self.payment_type if hasattr(self, "payment_type") else None)!r}, '
                f'created_at={self.created_at!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'subscription_id={self.subscription_id!s}, '
                f'amount_in_cents={self.amount_in_cents!s}, '
                f'remaining_amount_in_cents={self.remaining_amount_in_cents!s}, '
                f'refunded_amount_in_cents={(self.refunded_amount_in_cents if hasattr(self, "refunded_amount_in_cents") else None)!s}, '
                f'details={(self.details if hasattr(self, "details") else None)!s}, '
                f'external={self.external!s}, '
                f'memo={self.memo!s}, '
                f'payment_type={(self.payment_type if hasattr(self, "payment_type") else None)!s}, '
                f'created_at={self.created_at!s}, '
                f'additional_properties={self.additional_properties!s})')
