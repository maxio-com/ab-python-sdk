# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.update_price import UpdatePrice


class UpdateComponentPricePoint(object):

    """Implementation of the 'Update Component Price Point' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        prices (List[UpdatePrice]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "prices": 'prices'
    }

    _optionals = [
        'name',
        'prices',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 prices=APIHelper.SKIP):
        """Constructor for the UpdateComponentPricePoint class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [UpdatePrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   prices)
