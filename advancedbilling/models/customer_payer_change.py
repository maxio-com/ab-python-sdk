"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.invoice_payer_change import (
    InvoicePayerChange,
)


class CustomerPayerChange(object):
    """Implementation of the 'Customer Payer Change' model.

    Attributes:
        before (InvoicePayerChange): The model property of type InvoicePayerChange.
        after (InvoicePayerChange): The model property of type InvoicePayerChange.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": "before",
        "after": "after",
    }

    def __init__(
        self,
        before=None,
        after=None,
        additional_properties=None):
        """Initialize a CustomerPayerChange instance."""
        # Initialize members of the class
        self.before = before
        self.after = after

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
        before =\
            InvoicePayerChange.from_dictionary(
                dictionary.get("before"))\
                if dictionary.get("before") else None
        after =\
            InvoicePayerChange.from_dictionary(
                dictionary.get("after"))\
                if dictionary.get("after") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(before,
                   after,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _before=self.before
        _after=self.after
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"before={_before!r}, "
            f"after={_after!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _before=self.before
        _after=self.after
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"before={_before!s}, "
            f"after={_after!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
