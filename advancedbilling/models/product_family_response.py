# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.product_family import ProductFamily


class ProductFamilyResponse(object):

    """Implementation of the 'Product Family Response' model.

    TODO: type model description here.

    Attributes:
        product_family (ProductFamily): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_family": 'product_family'
    }

    _optionals = [
        'product_family',
    ]

    def __init__(self,
                 product_family=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ProductFamilyResponse class"""

        # Initialize members of the class
        if product_family is not APIHelper.SKIP:
            self.product_family = product_family 

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
        product_family = ProductFamily.from_dictionary(dictionary.get('product_family')) if 'product_family' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(product_family,
                   dictionary)
