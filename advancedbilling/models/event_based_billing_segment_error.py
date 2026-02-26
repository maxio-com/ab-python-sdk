"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class EventBasedBillingSegmentError(object):
    """Implementation of the 'Event Based Billing Segment Error' model.

    Attributes:
        segments (Dict[str, Any]): The key of the object would be a number (an index
            in the request array) where the error occurred. In the value object, the
            key represents the field and the value is an array with error messages.
            In most cases, this object would contain just one key.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segments": "segments",
    }

    def __init__(
        self,
        segments=None,
        additional_properties=None):
        """Initialize a EventBasedBillingSegmentError instance."""
        # Initialize members of the class
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
        segments =\
            dictionary.get("segments")\
            if dictionary.get("segments")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(segments,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _segments=self.segments
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"segments={_segments!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _segments=self.segments
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"segments={_segments!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
