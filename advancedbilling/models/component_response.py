# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.component import Component


class ComponentResponse(object):

    """Implementation of the 'Component Response' model.

    TODO: type model description here.

    Attributes:
        component (Component): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component": 'component'
    }

    def __init__(self,
                 component=None):
        """Constructor for the ComponentResponse class"""

        # Initialize members of the class
        self.component = component 

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
        component = Component.from_dictionary(dictionary.get('component')) if dictionary.get('component') else None
        # Return an object of this model
        return cls(component)
