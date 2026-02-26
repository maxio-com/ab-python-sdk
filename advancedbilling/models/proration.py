"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Proration(object):
    """Implementation of the 'Proration' model.

    Attributes:
        preserve_period (bool): The alternative to sending preserve_period as a
            direct attribute to migration
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "preserve_period": "preserve_period",
    }

    _optionals = [
        "preserve_period",
    ]

    def __init__(
        self,
        preserve_period=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Proration instance."""
        # Initialize members of the class
        if preserve_period is not APIHelper.SKIP:
            self.preserve_period = preserve_period

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
        preserve_period =\
            dictionary.get("preserve_period")\
            if "preserve_period" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(preserve_period,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _preserve_period=(
            self.preserve_period
            if hasattr(self, "preserve_period")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"preserve_period={_preserve_period!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _preserve_period=(
            self.preserve_period
            if hasattr(self, "preserve_period")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"preserve_period={_preserve_period!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
