# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price_point import ComponentPricePoint
from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta


class ComponentPricePointsResponse(object):

    """Implementation of the 'Component Price Points response' model.

    Attributes:
        price_points (List[ComponentPricePoint]): The model property of type
            List[ComponentPricePoint].
        meta (ListPublicKeysMeta): The model property of type
            ListPublicKeysMeta.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_points": 'price_points',
        "meta": 'meta'
    }

    _optionals = [
        'price_points',
        'meta',
    ]

    def __init__(self,
                 price_points=APIHelper.SKIP,
                 meta=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ComponentPricePointsResponse class"""

        # Initialize members of the class
        if price_points is not APIHelper.SKIP:
            self.price_points = price_points 
        if meta is not APIHelper.SKIP:
            self.meta = meta 

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
            price_points = [ComponentPricePoint.from_dictionary(x) for x in dictionary.get('price_points')]
        else:
            price_points = APIHelper.SKIP
        meta = ListPublicKeysMeta.from_dictionary(dictionary.get('meta')) if 'meta' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(price_points,
                   meta,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'price_points={(self.price_points if hasattr(self, "price_points") else None)!r}, '
                f'meta={(self.meta if hasattr(self, "meta") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'price_points={(self.price_points if hasattr(self, "price_points") else None)!s}, '
                f'meta={(self.meta if hasattr(self, "meta") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
