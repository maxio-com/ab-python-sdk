# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_metadata import CreateMetadata


class CreateMetadataRequest(object):

    """Implementation of the 'Create Metadata Request' model.

    Attributes:
        metadata (List[CreateMetadata]): The model property of type
            List[CreateMetadata].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata": 'metadata'
    }

    def __init__(self,
                 metadata=None,
                 additional_properties=None):
        """Constructor for the CreateMetadataRequest class"""

        # Initialize members of the class
        self.metadata = metadata 

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
        metadata = None
        if dictionary.get('metadata') is not None:
            metadata = [CreateMetadata.from_dictionary(x) for x in dictionary.get('metadata')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(metadata,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'metadata={self.metadata!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'metadata={self.metadata!s}, '
                f'additional_properties={self.additional_properties!s})')
