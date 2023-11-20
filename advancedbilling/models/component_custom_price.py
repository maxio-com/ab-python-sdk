# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price import Price


class ComponentCustomPrice(object):

    """Implementation of the 'Component Custom Price' model.

    Create or update custom pricing unique to the subscription. Used in place
    of `price_point_id`.

    Attributes:
        pricing_scheme (PricingScheme | None): Omit for On/Off components
        prices (List[Price]): On/off components only need one price bracket
            starting at 1

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices'
    }

    _optionals = [
        'pricing_scheme',
        'prices',
    ]

    def __init__(self,
                 pricing_scheme=APIHelper.SKIP,
                 prices=APIHelper.SKIP):
        """Constructor for the ComponentCustomPrice class"""

        # Initialize members of the class
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 

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
        pricing_scheme = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ComponentCustomPricePricingScheme'), dictionary.get('pricing_scheme'), False) if dictionary.get('pricing_scheme') is not None else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Return an object of this model
        return cls(pricing_scheme,
                   prices)

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
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
