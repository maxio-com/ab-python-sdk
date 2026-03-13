"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.base_string_error import (
    BaseStringError,
)


class ProformaError(object):
    """Implementation of the 'Proforma Error' model.

    Attributes:
        subscription (BaseStringError): The error is base if it is not directly
            associated with a single attribute.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription": "subscription",
    }

    _optionals = [
        "subscription",
    ]

    def __init__(
        self,
        subscription=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ProformaError instance."""
        # Initialize members of the class
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription

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
        subscription =\
            BaseStringError.from_dictionary(
                dictionary.get("subscription"))\
                if "subscription" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(subscription,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _subscription=(
            self.subscription
            if hasattr(self, "subscription")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription={_subscription!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _subscription=(
            self.subscription
            if hasattr(self, "subscription")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription={_subscription!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
