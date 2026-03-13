"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.send_email import (
    SendEmail,
)


class AvailableActions(object):
    """Implementation of the 'AvailableActions' model.

    Attributes:
        send_email (SendEmail): The model property of type SendEmail.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "send_email": "send_email",
    }

    _optionals = [
        "send_email",
    ]

    def __init__(
        self,
        send_email=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a AvailableActions instance."""
        # Initialize members of the class
        if send_email is not APIHelper.SKIP:
            self.send_email = send_email

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
        send_email =\
            SendEmail.from_dictionary(
                dictionary.get("send_email"))\
                if "send_email" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(send_email,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _send_email=(
            self.send_email
            if hasattr(self, "send_email")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"send_email={_send_email!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _send_email=(
            self.send_email
            if hasattr(self, "send_email")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"send_email={_send_email!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
