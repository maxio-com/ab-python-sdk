# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.quantity_based_component import QuantityBasedComponent


class CreateQuantityBasedComponent(object):

    """Implementation of the 'Create Quantity Based Component' model.

    TODO: type model description here.

    Attributes:
        quantity_based_component (QuantityBasedComponent): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity_based_component": 'quantity_based_component'
    }

    def __init__(self,
                 quantity_based_component=None):
        """Constructor for the CreateQuantityBasedComponent class"""

        # Initialize members of the class
        self.quantity_based_component = quantity_based_component 

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
        quantity_based_component = QuantityBasedComponent.from_dictionary(dictionary.get('quantity_based_component')) if dictionary.get('quantity_based_component') else None
        # Return an object of this model
        return cls(quantity_based_component)
