# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.product import Product


class ProductResponse(object):

    """Implementation of the 'Product Response' model.

    TODO: type model description here.

    Attributes:
        product (Product): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product": 'product'
    }

    def __init__(self,
                 product=None):
        """Constructor for the ProductResponse class"""

        # Initialize members of the class
        self.product = product 

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
        product = Product.from_dictionary(dictionary.get('product')) if dictionary.get('product') else None
        # Return an object of this model
        return cls(product)
