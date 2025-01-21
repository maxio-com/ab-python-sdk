# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metadata import Metadata


class PaginatedMetadata(object):

    """Implementation of the 'Paginated Metadata' model.

    Attributes:
        total_count (int): The model property of type int.
        current_page (int): The model property of type int.
        total_pages (int): The model property of type int.
        per_page (int): The model property of type int.
        metadata (List[Metadata]): The model property of type List[Metadata].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_count": 'total_count',
        "current_page": 'current_page',
        "total_pages": 'total_pages',
        "per_page": 'per_page',
        "metadata": 'metadata'
    }

    _optionals = [
        'total_count',
        'current_page',
        'total_pages',
        'per_page',
        'metadata',
    ]

    def __init__(self,
                 total_count=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 per_page=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PaginatedMetadata class"""

        # Initialize members of the class
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if metadata is not APIHelper.SKIP:
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
        total_count = dictionary.get("total_count") if dictionary.get("total_count") else APIHelper.SKIP
        current_page = dictionary.get("current_page") if dictionary.get("current_page") else APIHelper.SKIP
        total_pages = dictionary.get("total_pages") if dictionary.get("total_pages") else APIHelper.SKIP
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        metadata = None
        if dictionary.get('metadata') is not None:
            metadata = [Metadata.from_dictionary(x) for x in dictionary.get('metadata')]
        else:
            metadata = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(total_count,
                   current_page,
                   total_pages,
                   per_page,
                   metadata,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'total_count={self.total_count!r}, '
                f'current_page={self.current_page!r}, '
                f'total_pages={self.total_pages!r}, '
                f'per_page={self.per_page!r}, '
                f'metadata={self.metadata!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'total_count={self.total_count!s}, '
                f'current_page={self.current_page!s}, '
                f'total_pages={self.total_pages!s}, '
                f'per_page={self.per_page!s}, '
                f'metadata={self.metadata!s}, '
                f'additional_properties={self.additional_properties!s})')
