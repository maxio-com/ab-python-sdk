# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.ebb_component import EBBComponent


class CreateEBBComponent(object):

    """Implementation of the 'Create EBB Component' model.

    Attributes:
        event_based_component (EBBComponent): The model property of type
            EBBComponent.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event_based_component": 'event_based_component'
    }

    def __init__(self,
                 event_based_component=None,
                 additional_properties=None):
        """Constructor for the CreateEBBComponent class"""

        # Initialize members of the class
        self.event_based_component = event_based_component 

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
        event_based_component = EBBComponent.from_dictionary(dictionary.get('event_based_component')) if dictionary.get('event_based_component') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(event_based_component,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'event_based_component={self.event_based_component!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'event_based_component={self.event_based_component!s}, '
                f'additional_properties={self.additional_properties!s})')
