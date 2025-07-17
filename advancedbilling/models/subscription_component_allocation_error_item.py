# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionComponentAllocationErrorItem(object):

    """Implementation of the 'Subscription Component Allocation Error Item' model.

    Attributes:
        kind (str): The model property of type str.
        message (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kind": 'kind',
        "message": 'message'
    }

    _optionals = [
        'kind',
        'message',
    ]

    def __init__(self,
                 kind=APIHelper.SKIP,
                 message=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionComponentAllocationErrorItem class"""

        # Initialize members of the class
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if message is not APIHelper.SKIP:
            self.message = message 

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
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(kind,
                   message,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'kind={(self.kind if hasattr(self, "kind") else None)!r}, '
                f'message={(self.message if hasattr(self, "message") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'kind={(self.kind if hasattr(self, "kind") else None)!s}, '
                f'message={(self.message if hasattr(self, "message") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
