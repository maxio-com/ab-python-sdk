# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.on_off_component import OnOffComponent


class CreateOnOffComponent(object):

    """Implementation of the 'Create On/Off Component' model.

    Attributes:
        on_off_component (OnOffComponent): The model property of type
            OnOffComponent.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "on_off_component": 'on_off_component'
    }

    def __init__(self,
                 on_off_component=None,
                 additional_properties=None):
        """Constructor for the CreateOnOffComponent class"""

        # Initialize members of the class
        self.on_off_component = on_off_component 

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
        on_off_component = OnOffComponent.from_dictionary(dictionary.get('on_off_component')) if dictionary.get('on_off_component') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(on_off_component,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'on_off_component={self.on_off_component!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'on_off_component={self.on_off_component!s}, '
                f'additional_properties={self.additional_properties!s})')
