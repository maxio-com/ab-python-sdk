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

    Attributes:
        product_family (ProductFamily): The model property of type
            ProductFamily.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the ProductFamilyResponse class"""

        # Initialize members of the class
        if product_family is not APIHelper.SKIP:
            self.product_family = product_family 

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
        product_family = ProductFamily.from_dictionary(dictionary.get('product_family')) if 'product_family' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(product_family,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_family={self.product_family!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_family={self.product_family!s}, '
                f'additional_properties={self.additional_properties!s})')
