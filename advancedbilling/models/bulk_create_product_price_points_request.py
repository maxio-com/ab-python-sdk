# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_product_price_point import CreateProductPricePoint


class BulkCreateProductPricePointsRequest(object):

    """Implementation of the 'Bulk Create Product Price Points Request' model.

    Attributes:
        price_points (List[CreateProductPricePoint]): The model property of
            type List[CreateProductPricePoint].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_points": 'price_points'
    }

    def __init__(self,
                 price_points=None,
                 additional_properties=None):
        """Constructor for the BulkCreateProductPricePointsRequest class"""

        # Initialize members of the class
        self.price_points = price_points 

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
        price_points = None
        if dictionary.get('price_points') is not None:
            price_points = [CreateProductPricePoint.from_dictionary(x) for x in dictionary.get('price_points')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(price_points,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'price_points={self.price_points!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'price_points={self.price_points!s}, '
                f'additional_properties={self.additional_properties!s})')
