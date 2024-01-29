# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.component_price_point import ComponentPricePoint


class ListComponentsPricePointsResponse(object):

    """Implementation of the 'List Components Price Points Response' model.

    TODO: type model description here.

    Attributes:
        price_points (List[ComponentPricePoint]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_points": 'price_points'
    }

    def __init__(self,
                 price_points=None):
        """Constructor for the ListComponentsPricePointsResponse class"""

        # Initialize members of the class
        self.price_points = price_points 

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
        price_points = None
        if dictionary.get('price_points') is not None:
            price_points = [ComponentPricePoint.from_dictionary(x) for x in dictionary.get('price_points')]
        # Return an object of this model
        return cls(price_points)
