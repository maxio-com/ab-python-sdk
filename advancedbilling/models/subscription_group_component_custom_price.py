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
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): TODO: type description here.
        overage_pricing (List[ComponentCustomPrice]): TODO: type description
            here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 overage_pricing=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupComponentCustomPrice class"""

        # Initialize members of the class
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if overage_pricing is not APIHelper.SKIP:
            self.overage_pricing = overage_pricing 

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
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(pricing_scheme,
                   prices,
                   overage_pricing,
                   additional_properties)

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
