# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateComponentPricePointsRequest(object):

    """Implementation of the 'Create Component Price Points Request' model.

    TODO: type model description here.

    Attributes:
        price_points (List[CreateComponentPricePoint |
            CreatePrepaidUsageComponentPricePoint]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_points": 'price_points'
    }

    def __init__(self,
                 price_points=None):
        """Constructor for the CreateComponentPricePointsRequest class"""

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        price_points = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateComponentPricePointsRequestPricePoints'), dictionary.get('price_points'), False) if dictionary.get('price_points') is not None else None
        # Return an object of this model
        return cls(price_points)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('CreateComponentPricePointsRequestPricePoints').validate(dictionary.price_points)

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('CreateComponentPricePointsRequestPricePoints').validate(dictionary.get('price_points'))
