# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListSubscriptionGroupsMeta(object):

    """Implementation of the 'List Subscription Groups Meta' model.

    Attributes:
        current_page (int): The model property of type int.
        total_count (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_page": 'current_page',
        "total_count": 'total_count'
    }

    _optionals = [
        'current_page',
        'total_count',
    ]

    def __init__(self,
                 current_page=APIHelper.SKIP,
                 total_count=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListSubscriptionGroupsMeta class"""

        # Initialize members of the class
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 

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
        current_page = dictionary.get("current_page") if dictionary.get("current_page") else APIHelper.SKIP
        total_count = dictionary.get("total_count") if dictionary.get("total_count") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(current_page,
                   total_count,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!r}, '
                f'total_count={(self.total_count if hasattr(self, "total_count") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!s}, '
                f'total_count={(self.total_count if hasattr(self, "total_count") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
