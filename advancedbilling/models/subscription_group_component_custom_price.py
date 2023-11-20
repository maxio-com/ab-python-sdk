# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.price import Price


class SubscriptionGroupComponentCustomPrice(object):

    """Implementation of the 'Subscription Group Component Custom Price' model.

    Used in place of `price_point_id` to define a custom price point unique to
    the subscription. You still need to provide `component_id`.

    Attributes:
        pricing_scheme (PricingScheme | None): The identifier for the pricing
            scheme. See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): TODO: type description here.
        overage_pricing (List[ComponentCustomPrice]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "overage_pricing": 'overage_pricing'
    }

    _optionals = [
        'pricing_scheme',
        'prices',
        'overage_pricing',
    ]

    def __init__(self,
                 pricing_scheme=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 overage_pricing=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupComponentCustomPrice class"""

        # Initialize members of the class
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if overage_pricing is not APIHelper.SKIP:
            self.overage_pricing = overage_pricing 

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
        pricing_scheme = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupComponentCustomPricePricingScheme'), dictionary.get('pricing_scheme'), False) if dictionary.get('pricing_scheme') is not None else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        overage_pricing = None
        if dictionary.get('overage_pricing') is not None:
            overage_pricing = [ComponentCustomPrice.from_dictionary(x) for x in dictionary.get('overage_pricing')]
        else:
            overage_pricing = APIHelper.SKIP
        # Return an object of this model
        return cls(pricing_scheme,
                   prices,
                   overage_pricing)
