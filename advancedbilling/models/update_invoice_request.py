"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.update_invoice import (
    UpdateInvoice,
)


class UpdateInvoiceRequest(object):
    """Implementation of the 'Update Invoice Request' model.

    Request payload for updating a draft ad hoc invoice.

    Attributes:
        invoice (UpdateInvoice): Attributes of a draft ad hoc invoice which can be
            updated. Only the submitted attributes are changed.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice": "invoice",
    }

    def __init__(
        self,
        invoice=None,
        additional_properties=None):
        """Initialize a UpdateInvoiceRequest instance."""
        # Initialize members of the class
        self.invoice = invoice

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
        invoice =\
            UpdateInvoice.from_dictionary(
                dictionary.get("invoice"))\
                if dictionary.get("invoice") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(invoice,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _invoice=self.invoice
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"invoice={_invoice!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _invoice=self.invoice
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"invoice={_invoice!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
