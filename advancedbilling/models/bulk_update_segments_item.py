# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice


class BulkUpdateSegmentsItem(object):

    """Implementation of the 'Bulk Update Segments Item' model.

    TODO: type model description here.

    Attributes:
        id (int): The ID of the segment you want to update.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[CreateOrUpdateSegmentPrice]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices'
    }

    def __init__(self,
                 id=None,
                 pricing_scheme=None,
                 prices=None,
                 additional_properties={}):
        """Constructor for the BulkUpdateSegmentsItem class"""

        # Initialize members of the class
        self.id = id 
        self.pricing_scheme = pricing_scheme 
        self.prices = prices 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else None
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else None
        prices = None
        if dictionary.get('prices') is not None:
            prices = [CreateOrUpdateSegmentPrice.from_dictionary(x) for x in dictionary.get('prices')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   pricing_scheme,
                   prices,
                   dictionary)
