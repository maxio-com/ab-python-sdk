# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class MRRMovement(object):

    """Implementation of the 'MRR Movement' model.

    Attributes:
        amount (int): The model property of type int.
        category (str): The model property of type str.
        subscriber_delta (int): The model property of type int.
        lead_delta (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "category": 'category',
        "subscriber_delta": 'subscriber_delta',
        "lead_delta": 'lead_delta'
    }

    _optionals = [
        'amount',
        'category',
        'subscriber_delta',
        'lead_delta',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 subscriber_delta=APIHelper.SKIP,
                 lead_delta=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the MRRMovement class"""

        # Initialize members of the class
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if category is not APIHelper.SKIP:
            self.category = category 
        if subscriber_delta is not APIHelper.SKIP:
            self.subscriber_delta = subscriber_delta 
        if lead_delta is not APIHelper.SKIP:
            self.lead_delta = lead_delta 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        category = dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        subscriber_delta = dictionary.get("subscriber_delta") if dictionary.get("subscriber_delta") else APIHelper.SKIP
        lead_delta = dictionary.get("lead_delta") if dictionary.get("lead_delta") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount,
                   category,
                   subscriber_delta,
                   lead_delta,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'category={(self.category if hasattr(self, "category") else None)!r}, '
                f'subscriber_delta={(self.subscriber_delta if hasattr(self, "subscriber_delta") else None)!r}, '
                f'lead_delta={(self.lead_delta if hasattr(self, "lead_delta") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'category={(self.category if hasattr(self, "category") else None)!s}, '
                f'subscriber_delta={(self.subscriber_delta if hasattr(self, "subscriber_delta") else None)!s}, '
                f'lead_delta={(self.lead_delta if hasattr(self, "lead_delta") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
