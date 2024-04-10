# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PrepaidProductPricePointFilter(object):

    """Implementation of the 'Prepaid Product Price Point Filter' model.

    TODO: type model description here.

    Attributes:
        product_price_point_id (str): Passed as a parameter to list methods to
            return only non null values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_price_point_id": 'product_price_point_id'
    }

    def __init__(self,
                 additional_properties={}):
        """Constructor for the PrepaidProductPricePointFilter class"""

        # Initialize members of the class
        self.product_price_point_id = 'not_null' 

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

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(dictionary)
