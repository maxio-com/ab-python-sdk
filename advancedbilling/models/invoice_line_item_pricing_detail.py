"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class InvoiceLineItemPricingDetail(object):
    """Implementation of the 'Invoice Line Item Pricing Detail' model.

    Attributes:
        label (str): The model property of type str.
        amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "label": "label",
        "amount": "amount",
    }

    _optionals = [
        "label",
        "amount",
    ]

    def __init__(
        self,
        label=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a InvoiceLineItemPricingDetail instance."""
        # Initialize members of the class
        if label is not APIHelper.SKIP:
            self.label = label
        if amount is not APIHelper.SKIP:
            self.amount = amount

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
        label =\
            dictionary.get("label")\
            if dictionary.get("label")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(label,
                   amount,
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
        _label=(
            self.label
            if hasattr(self, "label")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"label={_label!r}, "
            f"amount={_amount!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _label=(
            self.label
            if hasattr(self, "label")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"label={_label!s}, "
            f"amount={_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
