"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class BillingSchedule(object):
    """Implementation of the 'Billing Schedule' model.

    Billing schedule settings for component allocations or usages on multi-frequency
    subscriptions. Use this to start a component's billing period on a custom date
    instead of aligning with the product charge schedule.

    Attributes:
        initial_billing_at (date): Custom start date (ISO 8601 date, YYYY-MM-DD) for
            the component's first billing period. If omitted or null, billing aligns
            with the product schedule. If provided, date must be on or after the
            minimum allowed date for the subscription or component.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_billing_at": "initial_billing_at",
    }

    _optionals = [
        "initial_billing_at",
    ]

    _nullables = [
        "initial_billing_at",
    ]

    def __init__(
        self,
        initial_billing_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BillingSchedule instance."""
        # Initialize members of the class
        if initial_billing_at is not APIHelper.SKIP:
            self.initial_billing_at = initial_billing_at

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
        if "initial_billing_at" in dictionary.keys():
            initial_billing_at = dateutil.parser.parse(
                dictionary.get("initial_billing_at")).date()\
                if dictionary.get("initial_billing_at") else None

        else:
            initial_billing_at = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(initial_billing_at,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _initial_billing_at=(
            self.initial_billing_at
            if hasattr(self, "initial_billing_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"initial_billing_at={_initial_billing_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _initial_billing_at=(
            self.initial_billing_at
            if hasattr(self, "initial_billing_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"initial_billing_at={_initial_billing_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
