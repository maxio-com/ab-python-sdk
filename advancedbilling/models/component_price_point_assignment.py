# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentPricePointAssignment(object):

    """Implementation of the 'Component Price Point Assignment' model.

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        price_point (str | int | None): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 price_point=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ComponentPricePointAssignment class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        price_point = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ComponentPricePointAssignmentPricePoint'), dictionary.get('price_point'), False) if dictionary.get('price_point') is not None else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   price_point,
                   additional_properties)
