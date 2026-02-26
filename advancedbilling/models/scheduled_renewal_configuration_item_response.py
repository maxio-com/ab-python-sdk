"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.scheduled_renewal_configuration_item import (
    ScheduledRenewalConfigurationItem,
)


class ScheduledRenewalConfigurationItemResponse(object):
    """Implementation of the 'Scheduled Renewal Configuration Item Response' model.

    Attributes:
        scheduled_renewal_configuration_item (ScheduledRenewalConfigurationItem): The
            model property of type ScheduledRenewalConfigurationItem.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheduled_renewal_configuration_item": "scheduled_renewal_configuration_item",
    }

    _optionals = [
        "scheduled_renewal_configuration_item",
    ]

    def __init__(
        self,
        scheduled_renewal_configuration_item=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalConfigurationItemResponse instance."""
        # Initialize members of the class
        if scheduled_renewal_configuration_item is not APIHelper.SKIP:
            self.scheduled_renewal_configuration_item =\
                 scheduled_renewal_configuration_item

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
        scheduled_renewal_configuration_item =\
            ScheduledRenewalConfigurationItem.from_dictionary(
                dictionary.get("scheduled_renewal_configuration_item"))\
                if "scheduled_renewal_configuration_item" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(scheduled_renewal_configuration_item,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _scheduled_renewal_configuration_item=(
            self.scheduled_renewal_configuration_item
            if hasattr(self, "scheduled_renewal_configuration_item")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"scheduled_renewal_configuration_item={_scheduled_renewal_configuration_item!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _scheduled_renewal_configuration_item=(
            self.scheduled_renewal_configuration_item
            if hasattr(self, "scheduled_renewal_configuration_item")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"scheduled_renewal_configuration_item={_scheduled_renewal_configuration_item!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
