# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateOfferComponent(object):

    """Implementation of the 'Create Offer Component' model.

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        price_point_id (int): TODO: type description here.
        starting_quantity (int): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "starting_quantity": 'starting_quantity'
    }

    _optionals = [
        'component_id',
        'price_point_id',
        'starting_quantity',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 starting_quantity=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateOfferComponent class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   price_point_id,
                   starting_quantity,
                   additional_properties)
