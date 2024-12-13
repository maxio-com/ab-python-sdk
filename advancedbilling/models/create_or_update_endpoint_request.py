# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_or_update_endpoint import CreateOrUpdateEndpoint


class CreateOrUpdateEndpointRequest(object):

    """Implementation of the 'Create or Update Endpoint Request' model.

    Used to Create or Update Endpoint

    Attributes:
        endpoint (CreateOrUpdateEndpoint): Used to Create or Update Endpoint
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint": 'endpoint'
    }

    def __init__(self,
                 endpoint=None,
                 additional_properties=None):
        """Constructor for the CreateOrUpdateEndpointRequest class"""

        # Initialize members of the class
        self.endpoint = endpoint 

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
        endpoint = CreateOrUpdateEndpoint.from_dictionary(dictionary.get('endpoint')) if dictionary.get('endpoint') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(endpoint,
                   additional_properties)
