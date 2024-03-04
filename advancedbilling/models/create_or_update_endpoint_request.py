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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint": 'endpoint'
    }

    def __init__(self,
                 endpoint=None,
                 additional_properties={}):
        """Constructor for the CreateOrUpdateEndpointRequest class"""

        # Initialize members of the class
        self.endpoint = endpoint 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        endpoint = CreateOrUpdateEndpoint.from_dictionary(dictionary.get('endpoint')) if dictionary.get('endpoint') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(endpoint,
                   dictionary)
