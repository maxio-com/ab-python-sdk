"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.list_proforma_invoices_meta import (
    ListProformaInvoicesMeta,
)
from advancedbilling.models.proforma_invoice import (
    ProformaInvoice,
)


class ListProformaInvoicesResponse(object):
    """Implementation of the 'List Proforma Invoices Response' model.

    Attributes:
        proforma_invoices (List[ProformaInvoice]): The model property of type
            List[ProformaInvoice].
        meta (ListProformaInvoicesMeta): The model property of type
            ListProformaInvoicesMeta.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "proforma_invoices": "proforma_invoices",
        "meta": "meta",
    }

    _optionals = [
        "proforma_invoices",
        "meta",
    ]

    def __init__(
        self,
        proforma_invoices=APIHelper.SKIP,
        meta=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ListProformaInvoicesResponse instance."""
        # Initialize members of the class
        if proforma_invoices is not APIHelper.SKIP:
            self.proforma_invoices = proforma_invoices
        if meta is not APIHelper.SKIP:
            self.meta = meta

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
        proforma_invoices = None
        if dictionary.get("proforma_invoices") is not None:
            proforma_invoices = [
                ProformaInvoice.from_dictionary(x)
                    for x in dictionary.get("proforma_invoices")
            ]
        else:
            proforma_invoices = APIHelper.SKIP
        meta =\
            ListProformaInvoicesMeta.from_dictionary(
                dictionary.get("meta"))\
                if "meta" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(proforma_invoices,
                   meta,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _proforma_invoices=(
            self.proforma_invoices
            if hasattr(self, "proforma_invoices")
            else None
        )
        _meta=(
            self.meta
            if hasattr(self, "meta")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"proforma_invoices={_proforma_invoices!r}, "
            f"meta={_meta!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _proforma_invoices=(
            self.proforma_invoices
            if hasattr(self, "proforma_invoices")
            else None
        )
        _meta=(
            self.meta
            if hasattr(self, "meta")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"proforma_invoices={_proforma_invoices!s}, "
            f"meta={_meta!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
