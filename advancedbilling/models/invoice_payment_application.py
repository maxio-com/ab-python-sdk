"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class InvoicePaymentApplication(object):
    """Implementation of the 'Invoice Payment Application' model.

    Attributes:
        invoice_uid (str): Unique identifier for the paid invoice. It has the prefix
            "inv_" followed by alphanumeric characters.
        application_uid (str): Unique identifier for the payment. It has the prefix
            "pmt_" followed by alphanumeric characters.
        applied_amount (str): Dollar amount of the paid invoice.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_uid": "invoice_uid",
        "application_uid": "application_uid",
        "applied_amount": "applied_amount",
    }

    _optionals = [
        "invoice_uid",
        "application_uid",
        "applied_amount",
    ]

    def __init__(
        self,
        invoice_uid=APIHelper.SKIP,
        application_uid=APIHelper.SKIP,
        applied_amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a InvoicePaymentApplication instance."""
        # Initialize members of the class
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid
        if application_uid is not APIHelper.SKIP:
            self.application_uid = application_uid
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount

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
        invoice_uid =\
            dictionary.get("invoice_uid")\
            if dictionary.get("invoice_uid")\
                else APIHelper.SKIP
        application_uid =\
            dictionary.get("application_uid")\
            if dictionary.get("application_uid")\
                else APIHelper.SKIP
        applied_amount =\
            dictionary.get("applied_amount")\
            if dictionary.get("applied_amount")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(invoice_uid,
                   application_uid,
                   applied_amount,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
            else None
        )
        _application_uid=(
            self.application_uid
            if hasattr(self, "application_uid")
            else None
        )
        _applied_amount=(
            self.applied_amount
            if hasattr(self, "applied_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"invoice_uid={_invoice_uid!r}, "
            f"application_uid={_application_uid!r}, "
            f"applied_amount={_applied_amount!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
            else None
        )
        _application_uid=(
            self.application_uid
            if hasattr(self, "application_uid")
            else None
        )
        _applied_amount=(
            self.applied_amount
            if hasattr(self, "applied_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"invoice_uid={_invoice_uid!s}, "
            f"application_uid={_application_uid!s}, "
            f"applied_amount={_applied_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
