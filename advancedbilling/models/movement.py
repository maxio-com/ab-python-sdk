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

    TODO: type model description here.

    Attributes:
        timestamp (datetime): TODO: type description here.
        amount_in_cents (long|int): TODO: type description here.
        amount_formatted (str): TODO: type description here.
        description (str): TODO: type description here.
        category (str): TODO: type description here.
        breakouts (Breakouts): TODO: type description here.
        line_items (List[MovementLineItem]): TODO: type description here.
        subscription_id (int): TODO: type description here.
        subscriber_name (str): TODO: type description here.

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
                 additional_properties={}):
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

        if dictionary is None:
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
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
                   dictionary)
