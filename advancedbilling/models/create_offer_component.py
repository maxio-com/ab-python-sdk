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
        starting_quantity (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "starting_quantity": 'starting_quantity'
    }

    _optionals = [
        'component_id',
        'starting_quantity',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 starting_quantity=APIHelper.SKIP):
        """Constructor for the CreateOfferComponent class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        # Return an object of this model
        return cls(component_id,
                   starting_quantity)
