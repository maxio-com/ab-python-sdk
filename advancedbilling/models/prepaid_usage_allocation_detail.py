"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class PrepaidUsageAllocationDetail(object):
    """Implementation of the 'Prepaid Usage Allocation Detail' model.

    Attributes:
        allocation_id (int): The model property of type int.
        charge_id (int): The model property of type int.
        usage_quantity (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocation_id": "allocation_id",
        "charge_id": "charge_id",
        "usage_quantity": "usage_quantity",
    }

    _optionals = [
        "allocation_id",
        "charge_id",
        "usage_quantity",
    ]

    def __init__(
        self,
        allocation_id=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        usage_quantity=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a PrepaidUsageAllocationDetail instance."""
        # Initialize members of the class
        if allocation_id is not APIHelper.SKIP:
            self.allocation_id = allocation_id
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if usage_quantity is not APIHelper.SKIP:
            self.usage_quantity = usage_quantity

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
        allocation_id =\
            dictionary.get("allocation_id")\
            if dictionary.get("allocation_id")\
                else APIHelper.SKIP
        charge_id =\
            dictionary.get("charge_id")\
            if dictionary.get("charge_id")\
                else APIHelper.SKIP
        usage_quantity =\
            dictionary.get("usage_quantity")\
            if dictionary.get("usage_quantity")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(allocation_id,
                   charge_id,
                   usage_quantity,
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
        _allocation_id=(
            self.allocation_id
            if hasattr(self, "allocation_id")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _usage_quantity=(
            self.usage_quantity
            if hasattr(self, "usage_quantity")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"allocation_id={_allocation_id!r}, "
            f"charge_id={_charge_id!r}, "
            f"usage_quantity={_usage_quantity!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _allocation_id=(
            self.allocation_id
            if hasattr(self, "allocation_id")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _usage_quantity=(
            self.usage_quantity
            if hasattr(self, "usage_quantity")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"allocation_id={_allocation_id!s}, "
            f"charge_id={_charge_id!s}, "
            f"usage_quantity={_usage_quantity!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
