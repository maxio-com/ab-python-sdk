# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.on_off_component import OnOffComponent


class CreateOnOffComponent(object):

    """Implementation of the 'Create On/Off Component' model.

    TODO: type model description here.

    Attributes:
        on_off_component (OnOffComponent): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "on_off_component": 'on_off_component'
    }

    def __init__(self,
                 on_off_component=None):
        """Constructor for the CreateOnOffComponent class"""

        # Initialize members of the class
        self.on_off_component = on_off_component 

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
        on_off_component = OnOffComponent.from_dictionary(dictionary.get('on_off_component')) if dictionary.get('on_off_component') else None
        # Return an object of this model
        return cls(on_off_component)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.on_off_component, type_callable=lambda value: OnOffComponent.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('on_off_component'), type_callable=lambda value: OnOffComponent.validate(value))
