# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.breakouts import Breakouts
from advancedbilling.models.movement_line_item import MovementLineItem


class Movement(object):

    """Implementation of the 'Movement' model.

    Attributes:
        timestamp (datetime): The model property of type datetime.
        amount_in_cents (int): The model property of type int.
        amount_formatted (str): The model property of type str.
        description (str): The model property of type str.
        category (str): The model property of type str.
        breakouts (Breakouts): The model property of type Breakouts.
        line_items (List[MovementLineItem]): The model property of type
            List[MovementLineItem].
        subscription_id (int): The model property of type int.
        subscriber_name (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp": 'timestamp',
        "amount_in_cents": 'amount_in_cents',
        "amount_formatted": 'amount_formatted',
        "description": 'description',
        "category": 'category',
        "breakouts": 'breakouts',
        "line_items": 'line_items',
        "subscription_id": 'subscription_id',
        "subscriber_name": 'subscriber_name'
    }

    _optionals = [
        'timestamp',
        'amount_in_cents',
        'amount_formatted',
        'description',
        'category',
        'breakouts',
        'line_items',
        'subscription_id',
        'subscriber_name',
    ]

    def __init__(self,
                 timestamp=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 amount_formatted=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 breakouts=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 subscriber_name=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Movement class"""

        # Initialize members of the class
        if timestamp is not APIHelper.SKIP:
            self.timestamp = APIHelper.apply_datetime_converter(timestamp, APIHelper.RFC3339DateTime) if timestamp else None 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted 
        if description is not APIHelper.SKIP:
            self.description = description 
        if category is not APIHelper.SKIP:
            self.category = category 
        if breakouts is not APIHelper.SKIP:
            self.breakouts = breakouts 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if subscriber_name is not APIHelper.SKIP:
            self.subscriber_name = subscriber_name 

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
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        amount_formatted = dictionary.get("amount_formatted") if dictionary.get("amount_formatted") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        category = dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        breakouts = Breakouts.from_dictionary(dictionary.get('breakouts')) if 'breakouts' in dictionary.keys() else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [MovementLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        subscriber_name = dictionary.get("subscriber_name") if dictionary.get("subscriber_name") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(timestamp,
                   amount_in_cents,
                   amount_formatted,
                   description,
                   category,
                   breakouts,
                   line_items,
                   subscription_id,
                   subscriber_name,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'timestamp={(self.timestamp if hasattr(self, "timestamp") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'amount_formatted={(self.amount_formatted if hasattr(self, "amount_formatted") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'category={(self.category if hasattr(self, "category") else None)!r}, '
                f'breakouts={(self.breakouts if hasattr(self, "breakouts") else None)!r}, '
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'subscriber_name={(self.subscriber_name if hasattr(self, "subscriber_name") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'timestamp={(self.timestamp if hasattr(self, "timestamp") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'amount_formatted={(self.amount_formatted if hasattr(self, "amount_formatted") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'category={(self.category if hasattr(self, "category") else None)!s}, '
                f'breakouts={(self.breakouts if hasattr(self, "breakouts") else None)!s}, '
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'subscriber_name={(self.subscriber_name if hasattr(self, "subscriber_name") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
