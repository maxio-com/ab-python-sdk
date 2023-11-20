# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.price import Price


class PrepaidComponentPricePoint(object):

    """Implementation of the 'Prepaid Component Price Point' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        pricing_scheme (str): TODO: type description here.
        prices (List[Price]): TODO: type description here.
        overage_pricing (OveragePricing): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "overage_pricing": 'overage_pricing'
    }

    _optionals = [
        'name',
        'handle',
        'pricing_scheme',
        'prices',
        'overage_pricing',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 overage_pricing=APIHelper.SKIP):
        """Constructor for the PrepaidComponentPricePoint class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        overage_pricing = OveragePricing.from_dictionary(dictionary.get('overage_pricing')) if 'overage_pricing' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   handle,
                   pricing_scheme,
                   prices,
                   overage_pricing)
