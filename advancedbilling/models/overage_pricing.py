# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme


class OveragePricing(object):

    """Implementation of the 'Overage Pricing' model.

    TODO: type model description here.

    Attributes:
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices'
    }

    _optionals = [
        'prices',
    ]

    def __init__(self,
                 pricing_scheme=None,
                 prices=APIHelper.SKIP):
        """Constructor for the OveragePricing class"""

        # Initialize members of the class
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
        pricing_scheme = APIHelper.deserialize_union_type(UnionTypeLookUp.get('OveragePricingPricingScheme'), dictionary.get('pricing_scheme'), False) if dictionary.get('pricing_scheme') is not None else None
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('OveragePricingPricingScheme').validate(dictionary.pricing_scheme)

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('OveragePricingPricingScheme').validate(dictionary.get('pricing_scheme'))
