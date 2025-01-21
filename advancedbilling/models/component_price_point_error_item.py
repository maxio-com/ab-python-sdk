# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentPricePointErrorItem(object):

    """Implementation of the 'Component PricePoint Error Item' model.

    Attributes:
        component_id (int): The model property of type int.
        message (str): The model property of type str.
        price_point (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "message": 'message',
        "price_point": 'price_point'
    }

    _optionals = [
        'component_id',
        'message',
        'price_point',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 message=APIHelper.SKIP,
                 price_point=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ComponentPricePointErrorItem class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if message is not APIHelper.SKIP:
            self.message = message 
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        price_point = dictionary.get("price_point") if dictionary.get("price_point") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   message,
                   price_point,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={self.component_id!r}, '
                f'message={self.message!r}, '
                f'price_point={self.price_point!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={self.component_id!s}, '
                f'message={self.message!s}, '
                f'price_point={self.price_point!s}, '
                f'additional_properties={self.additional_properties!s})')
