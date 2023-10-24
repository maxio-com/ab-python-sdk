# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.update_endpoint import UpdateEndpoint


class UpdateEndpointRequest(object):

    """Implementation of the 'Update Endpoint Request' model.

    Used to Create or Update Endpoint

    Attributes:
        endpoint (UpdateEndpoint): Used to Create or Update Endpoint

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint": 'endpoint'
    }

    def __init__(self,
                 endpoint=None):
        """Constructor for the UpdateEndpointRequest class"""

        # Initialize members of the class
        self.endpoint = endpoint 

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
        endpoint = UpdateEndpoint.from_dictionary(dictionary.get('endpoint')) if dictionary.get('endpoint') else None
        # Return an object of this model
        return cls(endpoint)
