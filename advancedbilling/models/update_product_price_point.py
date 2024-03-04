# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateProductPricePoint(object):

    """Implementation of the 'Update Product Price Point' model.

    TODO: type model description here.

    Attributes:
        handle (str): TODO: type description here.
        price_in_cents (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "handle": 'handle',
        "price_in_cents": 'price_in_cents'
    }

    _optionals = [
        'handle',
        'price_in_cents',
    ]

    def __init__(self,
                 handle=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the UpdateProductPricePoint class"""

        # Initialize members of the class
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if price_in_cents is not APIHelper.SKIP:
            self.price_in_cents = price_in_cents 

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
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(handle,
                   price_in_cents,
                   dictionary)
