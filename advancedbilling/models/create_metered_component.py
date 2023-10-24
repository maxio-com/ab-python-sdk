# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metered_component import MeteredComponent


class CreateMeteredComponent(object):

    """Implementation of the 'Create Metered Component' model.

    TODO: type model description here.

    Attributes:
        metered_component (MeteredComponent): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metered_component": 'metered_component'
    }

    def __init__(self,
                 metered_component=None):
        """Constructor for the CreateMeteredComponent class"""

        # Initialize members of the class
        self.metered_component = metered_component 

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
        metered_component = MeteredComponent.from_dictionary(dictionary.get('metered_component')) if dictionary.get('metered_component') else None
        # Return an object of this model
        return cls(metered_component)

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
            return APIHelper.is_valid_type(value=dictionary.metered_component, type_callable=lambda value: MeteredComponent.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('metered_component'), type_callable=lambda value: MeteredComponent.validate(value))
