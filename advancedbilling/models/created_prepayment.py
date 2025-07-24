# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreatedPrepayment(object):

    """Implementation of the 'Created Prepayment' model.

    Attributes:
        id (int): The model property of type int.
        subscription_id (int): The model property of type int.
        amount_in_cents (int): The model property of type int.
        memo (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        starting_balance_in_cents (int): The model property of type int.
        ending_balance_in_cents (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "subscription_id": 'subscription_id',
        "amount_in_cents": 'amount_in_cents',
        "memo": 'memo',
        "created_at": 'created_at',
        "starting_balance_in_cents": 'starting_balance_in_cents',
        "ending_balance_in_cents": 'ending_balance_in_cents'
    }

    _optionals = [
        'id',
        'subscription_id',
        'amount_in_cents',
        'memo',
        'created_at',
        'starting_balance_in_cents',
        'ending_balance_in_cents',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 starting_balance_in_cents=APIHelper.SKIP,
                 ending_balance_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreatedPrepayment class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if starting_balance_in_cents is not APIHelper.SKIP:
            self.starting_balance_in_cents = starting_balance_in_cents 
        if ending_balance_in_cents is not APIHelper.SKIP:
            self.ending_balance_in_cents = ending_balance_in_cents 

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
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        starting_balance_in_cents = dictionary.get("starting_balance_in_cents") if dictionary.get("starting_balance_in_cents") else APIHelper.SKIP
        ending_balance_in_cents = dictionary.get("ending_balance_in_cents") if dictionary.get("ending_balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   subscription_id,
                   amount_in_cents,
                   memo,
                   created_at,
                   starting_balance_in_cents,
                   ending_balance_in_cents,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'starting_balance_in_cents={(self.starting_balance_in_cents if hasattr(self, "starting_balance_in_cents") else None)!r}, '
                f'ending_balance_in_cents={(self.ending_balance_in_cents if hasattr(self, "ending_balance_in_cents") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'starting_balance_in_cents={(self.starting_balance_in_cents if hasattr(self, "starting_balance_in_cents") else None)!s}, '
                f'ending_balance_in_cents={(self.ending_balance_in_cents if hasattr(self, "ending_balance_in_cents") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
