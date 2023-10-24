# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_metadata import CreateMetadata


class CreateMetadataRequest(object):

    """Implementation of the 'Create Metadata Request' model.

    TODO: type model description here.

    Attributes:
        metadata (List[CreateMetadata]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata": 'metadata'
    }

    def __init__(self,
                 metadata=None):
        """Constructor for the CreateMetadataRequest class"""

        # Initialize members of the class
        self.metadata = metadata 

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
        metadata = None
        if dictionary.get('metadata') is not None:
            metadata = [CreateMetadata.from_dictionary(x) for x in dictionary.get('metadata')]
        # Return an object of this model
        return cls(metadata)
