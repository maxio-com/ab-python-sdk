# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.prepaid_usage_component import PrepaidUsageComponent


class CreatePrepaidComponent(object):

    """Implementation of the 'Create Prepaid Component' model.

    TODO: type model description here.

    Attributes:
        prepaid_usage_component (PrepaidUsageComponent): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepaid_usage_component": 'prepaid_usage_component'
    }

    def __init__(self,
                 prepaid_usage_component=None):
        """Constructor for the CreatePrepaidComponent class"""

        # Initialize members of the class
        self.prepaid_usage_component = prepaid_usage_component 

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
        prepaid_usage_component = PrepaidUsageComponent.from_dictionary(dictionary.get('prepaid_usage_component')) if dictionary.get('prepaid_usage_component') else None
        # Return an object of this model
        return cls(prepaid_usage_component)

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
            return APIHelper.is_valid_type(value=dictionary.prepaid_usage_component, type_callable=lambda value: PrepaidUsageComponent.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('prepaid_usage_component'), type_callable=lambda value: PrepaidUsageComponent.validate(value))
