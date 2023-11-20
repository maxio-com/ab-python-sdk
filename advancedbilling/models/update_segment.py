# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice


class UpdateSegment(object):

    """Implementation of the 'Update Segment' model.

    TODO: type model description here.

    Attributes:
        pricing_scheme (str): The handle for the pricing scheme. Available
            options: per_unit, volume, tiered, stairstep. See [Price Bracket
            Rules](https://help.chargify.com/products/product-components.html#p
            rice-bracket-rules) for an overview of pricing schemes.
        prices (List[CreateOrUpdateSegmentPrice]): TODO: type description
            here.

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
        """Constructor for the UpdateSegment class"""

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else None
        prices = None
        if dictionary.get('prices') is not None:
            prices = [CreateOrUpdateSegmentPrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Return an object of this model
        return cls(pricing_scheme,
                   prices)
