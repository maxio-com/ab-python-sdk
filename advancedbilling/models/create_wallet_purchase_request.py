"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.purchase import (
    Purchase,
)


class CreateWalletPurchaseRequest(object):
    """Implementation of the 'Create Wallet Purchase Request' model.

    Purchases prepaid units for the wallet at a price point, charging the
    subscription's payment method.

    Attributes:
        purchase (Purchase): The model property of type Purchase.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "purchase": "purchase",
    }

    def __init__(
        self,
        purchase=None,
        additional_properties=None):
        """Initialize a CreateWalletPurchaseRequest instance."""
        # Initialize members of the class
        self.purchase = purchase

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
        purchase =\
            Purchase.from_dictionary(
                dictionary.get("purchase"))\
                if dictionary.get("purchase") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(purchase,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _purchase=self.purchase
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"purchase={_purchase!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _purchase=self.purchase
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"purchase={_purchase!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
