# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentSPricePointAssignment(object):

    """Implementation of the 'Component's Price Point Assignment' model.

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        price_point (str | int | None): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "price_point": 'price_point'
    }

    _optionals = [
        'component_id',
        'price_point',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 price_point=APIHelper.SKIP):
        """Constructor for the ComponentSPricePointAssignment class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        price_point = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ComponentSPricePointAssignmentPricePoint'), dictionary.get('price_point'), False) if dictionary.get('price_point') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(component_id,
                   price_point)
