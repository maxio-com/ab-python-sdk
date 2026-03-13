"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class EnableWebhooksResponse(object):
    """Implementation of the 'Enable Webhooks Response' model.

    Attributes:
        webhooks_enabled (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "webhooks_enabled": "webhooks_enabled",
    }

    _optionals = [
        "webhooks_enabled",
    ]

    def __init__(
        self,
        webhooks_enabled=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a EnableWebhooksResponse instance."""
        # Initialize members of the class
        if webhooks_enabled is not APIHelper.SKIP:
            self.webhooks_enabled = webhooks_enabled

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
        webhooks_enabled =\
            dictionary.get("webhooks_enabled")\
            if "webhooks_enabled" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(webhooks_enabled,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _webhooks_enabled=(
            self.webhooks_enabled
            if hasattr(self, "webhooks_enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"webhooks_enabled={_webhooks_enabled!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _webhooks_enabled=(
            self.webhooks_enabled
            if hasattr(self, "webhooks_enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"webhooks_enabled={_webhooks_enabled!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
