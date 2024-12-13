# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Errors(object):

    """Implementation of the 'Errors' model.

    TODO: type model description here.

    Attributes:
        per_page (List[str]): TODO: type description here.
        price_point (List[str]): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "per_page": 'per_page',
        "price_point": 'price_point'
    }

    _optionals = [
        'per_page',
        'price_point',
    ]

    def __init__(self,
                 per_page=APIHelper.SKIP,
                 price_point=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Errors class"""

        # Initialize members of the class
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point 

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
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        price_point = dictionary.get("price_point") if dictionary.get("price_point") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(per_page,
                   price_point,
                   additional_properties)
