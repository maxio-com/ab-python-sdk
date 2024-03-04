# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_product_family import CreateProductFamily


class CreateProductFamilyRequest(object):

    """Implementation of the 'Create Product Family Request' model.

    TODO: type model description here.

    Attributes:
        product_family (CreateProductFamily): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_family": 'product_family'
    }

    def __init__(self,
                 product_family=None,
                 additional_properties={}):
        """Constructor for the CreateProductFamilyRequest class"""

        # Initialize members of the class
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
        product_family = CreateProductFamily.from_dictionary(dictionary.get('product_family')) if dictionary.get('product_family') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(product_family,
                   dictionary)
