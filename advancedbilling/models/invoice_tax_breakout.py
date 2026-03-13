"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class InvoiceTaxBreakout(object):
    """Implementation of the 'Invoice Tax Breakout' model.

    Attributes:
        uid (str): The model property of type str.
        taxable_amount (str): The model property of type str.
        tax_amount (str): The model property of type str.
        tax_exempt_amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": "uid",
        "taxable_amount": "taxable_amount",
        "tax_amount": "tax_amount",
        "tax_exempt_amount": "tax_exempt_amount",
    }

    _optionals = [
        "uid",
        "taxable_amount",
        "tax_amount",
        "tax_exempt_amount",
    ]

    def __init__(
        self,
        uid=APIHelper.SKIP,
        taxable_amount=APIHelper.SKIP,
        tax_amount=APIHelper.SKIP,
        tax_exempt_amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a InvoiceTaxBreakout instance."""
        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount
        if tax_exempt_amount is not APIHelper.SKIP:
            self.tax_exempt_amount = tax_exempt_amount

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
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else APIHelper.SKIP
        taxable_amount =\
            dictionary.get("taxable_amount")\
            if dictionary.get("taxable_amount")\
                else APIHelper.SKIP
        tax_amount =\
            dictionary.get("tax_amount")\
            if dictionary.get("tax_amount")\
                else APIHelper.SKIP
        tax_exempt_amount =\
            dictionary.get("tax_exempt_amount")\
            if dictionary.get("tax_exempt_amount")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(uid,
                   taxable_amount,
                   tax_amount,
                   tax_exempt_amount,
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
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _taxable_amount=(
            self.taxable_amount
            if hasattr(self, "taxable_amount")
            else None
        )
        _tax_amount=(
            self.tax_amount
            if hasattr(self, "tax_amount")
            else None
        )
        _tax_exempt_amount=(
            self.tax_exempt_amount
            if hasattr(self, "tax_exempt_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"taxable_amount={_taxable_amount!r}, "
            f"tax_amount={_tax_amount!r}, "
            f"tax_exempt_amount={_tax_exempt_amount!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _taxable_amount=(
            self.taxable_amount
            if hasattr(self, "taxable_amount")
            else None
        )
        _tax_amount=(
            self.tax_amount
            if hasattr(self, "tax_amount")
            else None
        )
        _tax_exempt_amount=(
            self.tax_exempt_amount
            if hasattr(self, "tax_exempt_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"taxable_amount={_taxable_amount!s}, "
            f"tax_amount={_tax_amount!s}, "
            f"tax_exempt_amount={_tax_exempt_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
