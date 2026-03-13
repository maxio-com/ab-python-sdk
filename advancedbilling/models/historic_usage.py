"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class HistoricUsage(object):
    """Implementation of the 'Historic Usage' model.

    Optional for Event Based Components. If the `include=historic_usages` query param
    is provided, the last ten billing periods will be returned.

    Attributes:
        total_usage_quantity (float): Total usage of a component for billing period
        billing_period_starts_at (datetime): Start date of billing period
        billing_period_ends_at (datetime): End date of billing period
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_usage_quantity": "total_usage_quantity",
        "billing_period_starts_at": "billing_period_starts_at",
        "billing_period_ends_at": "billing_period_ends_at",
    }

    _optionals = [
        "total_usage_quantity",
        "billing_period_starts_at",
        "billing_period_ends_at",
    ]

    def __init__(
        self,
        total_usage_quantity=APIHelper.SKIP,
        billing_period_starts_at=APIHelper.SKIP,
        billing_period_ends_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a HistoricUsage instance."""
        # Initialize members of the class
        if total_usage_quantity is not APIHelper.SKIP:
            self.total_usage_quantity = total_usage_quantity
        if billing_period_starts_at is not APIHelper.SKIP:
            self.billing_period_starts_at =\
                 APIHelper.apply_datetime_converter(
                billing_period_starts_at, APIHelper.RFC3339DateTime)\
                 if billing_period_starts_at else None
        if billing_period_ends_at is not APIHelper.SKIP:
            self.billing_period_ends_at =\
                 APIHelper.apply_datetime_converter(
                billing_period_ends_at, APIHelper.RFC3339DateTime)\
                 if billing_period_ends_at else None

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
        total_usage_quantity =\
            dictionary.get("total_usage_quantity")\
            if dictionary.get("total_usage_quantity")\
                else APIHelper.SKIP
        billing_period_starts_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("billing_period_starts_at")).datetime\
            if dictionary.get("billing_period_starts_at") else APIHelper.SKIP
        billing_period_ends_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("billing_period_ends_at")).datetime\
            if dictionary.get("billing_period_ends_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(total_usage_quantity,
                   billing_period_starts_at,
                   billing_period_ends_at,
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
        _total_usage_quantity=(
            self.total_usage_quantity
            if hasattr(self, "total_usage_quantity")
            else None
        )
        _billing_period_starts_at=(
            self.billing_period_starts_at
            if hasattr(self, "billing_period_starts_at")
            else None
        )
        _billing_period_ends_at=(
            self.billing_period_ends_at
            if hasattr(self, "billing_period_ends_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"total_usage_quantity={_total_usage_quantity!r}, "
            f"billing_period_starts_at={_billing_period_starts_at!r}, "
            f"billing_period_ends_at={_billing_period_ends_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _total_usage_quantity=(
            self.total_usage_quantity
            if hasattr(self, "total_usage_quantity")
            else None
        )
        _billing_period_starts_at=(
            self.billing_period_starts_at
            if hasattr(self, "billing_period_starts_at")
            else None
        )
        _billing_period_ends_at=(
            self.billing_period_ends_at
            if hasattr(self, "billing_period_ends_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"total_usage_quantity={_total_usage_quantity!s}, "
            f"billing_period_starts_at={_billing_period_starts_at!s}, "
            f"billing_period_ends_at={_billing_period_ends_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
