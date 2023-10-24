# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.update_component_price_point import UpdateComponentPricePoint


class UpdateComponentPricePointRequest(object):

    """Implementation of the 'Update Component Price Point Request' model.

    TODO: type model description here.

    Attributes:
        price_point (UpdateComponentPricePoint): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_point": 'price_point'
    }

    _optionals = [
        'price_point',
    ]

    def __init__(self,
                 price_point=APIHelper.SKIP):
        """Constructor for the UpdateComponentPricePointRequest class"""

        # Initialize members of the class
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point 

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
        price_point = UpdateComponentPricePoint.from_dictionary(dictionary.get('price_point')) if 'price_point' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(price_point)
