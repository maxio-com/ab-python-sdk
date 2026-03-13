"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.group_billing import (
    GroupBilling,
)
from advancedbilling.models.group_target import (
    GroupTarget,
)


class GroupSettings(object):
    """Implementation of the 'Group Settings' model.

    Attributes:
        target (GroupTarget): Attributes of the target customer who will be the
            responsible payer of the created subscription. Required.
        billing (GroupBilling): Optional attributes related to billing date and
            accrual. Note: Only applicable for new subscriptions.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "target": "target",
        "billing": "billing",
    }

    _optionals = [
        "billing",
    ]

    def __init__(
        self,
        target=None,
        billing=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a GroupSettings instance."""
        # Initialize members of the class
        self.target = target
        if billing is not APIHelper.SKIP:
            self.billing = billing

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
        target =\
            GroupTarget.from_dictionary(
                dictionary.get("target"))\
                if dictionary.get("target") else None
        billing =\
            GroupBilling.from_dictionary(
                dictionary.get("billing"))\
                if "billing" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(target,
                   billing,
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
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.target,
                    type_callable=lambda value:
                        GroupTarget.validate(value),
                    is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("target"),
                type_callable=lambda value:
                    GroupTarget.validate(value),
                is_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _target=self.target
        _billing=(
            self.billing
            if hasattr(self, "billing")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"target={_target!r}, "
            f"billing={_billing!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _target=self.target
        _billing=(
            self.billing
            if hasattr(self, "billing")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"target={_target!s}, "
            f"billing={_billing!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
