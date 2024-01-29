# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_usage import CreateUsage


class CreateUsageRequest(object):

    """Implementation of the 'Create Usage Request' model.

    TODO: type model description here.

    Attributes:
        usage (CreateUsage): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "usage": 'usage'
    }

    def __init__(self,
                 usage=None):
        """Constructor for the CreateUsageRequest class"""

        # Initialize members of the class
        self.usage = usage 

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
        usage = CreateUsage.from_dictionary(dictionary.get('usage')) if dictionary.get('usage') else None
        # Return an object of this model
        return cls(usage)
