"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ScheduledRenewalUpdateRequest(object):
    """Implementation of the 'Scheduled Renewal Update Request' model.

    Attributes:
        renewal_configuration_item (ScheduledRenewalItemRequestBodyComponent |
            ScheduledRenewalItemRequestBodyProduct): The model property of type
            ScheduledRenewalItemRequestBodyComponent |
            ScheduledRenewalItemRequestBodyProduct.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "renewal_configuration_item": "renewal_configuration_item",
    }

    def __init__(
        self,
        renewal_configuration_item=None,
        additional_properties=None):
        """Initialize a ScheduledRenewalUpdateRequest instance."""
        # Initialize members of the class
        self.renewal_configuration_item = renewal_configuration_item

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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        renewal_configuration_item = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("ScheduledRenewalUpdateRequestRenewalConfigurationItem"),
            dictionary.get("renewal_configuration_item"),
            False)\
            if dictionary.get("renewal_configuration_item") is not None\
            else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(renewal_configuration_item,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if isinstance(dictionary, cls):
            return (UnionTypeLookUp.get("ScheduledRenewalUpdateRequestRenewalConfigurationItem")
                .validate(dictionary.renewal_configuration_item).is_valid)

        if not isinstance(dictionary, dict):
            return False

        return (UnionTypeLookUp.get("ScheduledRenewalUpdateRequestRenewalConfigurationItem")
            .validate(dictionary.get("renewal_configuration_item")).is_valid)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _renewal_configuration_item=self.renewal_configuration_item
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"renewal_configuration_item={_renewal_configuration_item!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _renewal_configuration_item=self.renewal_configuration_item
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"renewal_configuration_item={_renewal_configuration_item!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
