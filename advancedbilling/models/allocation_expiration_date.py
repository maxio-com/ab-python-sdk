"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class AllocationExpirationDate(object):
    """Implementation of the 'Allocation Expiration Date' model.

    Attributes:
        expires_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expires_at": "expires_at",
    }

    _optionals = [
        "expires_at",
    ]

    def __init__(
        self,
        expires_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a AllocationExpirationDate instance."""
        # Initialize members of the class
        if expires_at is not APIHelper.SKIP:
            self.expires_at =\
                 APIHelper.apply_datetime_converter(
                expires_at, APIHelper.RFC3339DateTime)\
                 if expires_at else None

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
        expires_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("expires_at")).datetime\
            if dictionary.get("expires_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(expires_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"expires_at={_expires_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"expires_at={_expires_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
