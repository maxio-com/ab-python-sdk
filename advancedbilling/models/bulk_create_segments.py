"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_segment import (
    CreateSegment,
)


class BulkCreateSegments(object):
    """Implementation of the 'Bulk Create Segments' model.

    Attributes:
        segments (List[CreateSegment]): The model property of type
            List[CreateSegment].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segments": "segments",
    }

    _optionals = [
        "segments",
    ]

    def __init__(
        self,
        segments=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BulkCreateSegments instance."""
        # Initialize members of the class
        if segments is not APIHelper.SKIP:
            self.segments = segments

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        segments = None
        if dictionary.get("segments") is not None:
            segments = [
                CreateSegment.from_dictionary(x)
                    for x in dictionary.get("segments")
            ]
        else:
            segments = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(segments,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _segments=(
            self.segments
            if hasattr(self, "segments")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"segments={_segments!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _segments=(
            self.segments
            if hasattr(self, "segments")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"segments={_segments!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
