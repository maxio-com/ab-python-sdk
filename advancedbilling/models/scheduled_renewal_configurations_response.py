"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.scheduled_renewal_configuration import (
    ScheduledRenewalConfiguration,
)


class ScheduledRenewalConfigurationsResponse(object):
    """Implementation of the 'Scheduled Renewal Configurations Response' model.

    Attributes:
        scheduled_renewal_configurations (List[ScheduledRenewalConfiguration]): The
            model property of type List[ScheduledRenewalConfiguration].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheduled_renewal_configurations": "scheduled_renewal_configurations",
    }

    _optionals = [
        "scheduled_renewal_configurations",
    ]

    def __init__(
        self,
        scheduled_renewal_configurations=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalConfigurationsResponse instance."""
        # Initialize members of the class
        if scheduled_renewal_configurations is not APIHelper.SKIP:
            self.scheduled_renewal_configurations = scheduled_renewal_configurations

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
        scheduled_renewal_configurations = None
        if dictionary.get("scheduled_renewal_configurations") is not None:
            scheduled_renewal_configurations = [
                ScheduledRenewalConfiguration.from_dictionary(x)
                    for x in dictionary.get("scheduled_renewal_configurations")
            ]
        else:
            scheduled_renewal_configurations = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(scheduled_renewal_configurations,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _scheduled_renewal_configurations=(
            self.scheduled_renewal_configurations
            if hasattr(self, "scheduled_renewal_configurations")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"scheduled_renewal_configurations={_scheduled_renewal_configurations!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _scheduled_renewal_configurations=(
            self.scheduled_renewal_configurations
            if hasattr(self, "scheduled_renewal_configurations")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"scheduled_renewal_configurations={_scheduled_renewal_configurations!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
