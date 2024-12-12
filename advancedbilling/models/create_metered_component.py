# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.metered_component import MeteredComponent


class CreateMeteredComponent(object):

    """Implementation of the 'Create Metered Component' model.

    TODO: type model description here.

    Attributes:
        metered_component (MeteredComponent): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metered_component": 'metered_component'
    }

    def __init__(self,
                 metered_component=None,
                 additional_properties=None):
        """Constructor for the CreateMeteredComponent class"""

        # Initialize members of the class
        self.metered_component = metered_component 

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
        metered_component = MeteredComponent.from_dictionary(dictionary.get('metered_component')) if dictionary.get('metered_component') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(metered_component,
                   additional_properties)
