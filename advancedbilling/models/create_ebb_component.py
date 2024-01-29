# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.ebb_component import EBBComponent


class CreateEBBComponent(object):

    """Implementation of the 'Create EBB Component' model.

    TODO: type model description here.

    Attributes:
        event_based_component (EBBComponent): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event_based_component": 'event_based_component'
    }

    def __init__(self,
                 event_based_component=None):
        """Constructor for the CreateEBBComponent class"""

        # Initialize members of the class
        self.event_based_component = event_based_component 

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
        event_based_component = EBBComponent.from_dictionary(dictionary.get('event_based_component')) if dictionary.get('event_based_component') else None
        # Return an object of this model
        return cls(event_based_component)
