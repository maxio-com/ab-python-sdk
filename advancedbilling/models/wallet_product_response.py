"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.component import (
    Component,
)


class WalletProductResponse(object):
    """Implementation of the 'Wallet Product Response' model.

    A Wallet Product is a Component created with no product family, so it returns the
    full Component field set under a `wallet_product` root instead of `component`.

    Attributes:
        wallet_product (Component): The model property of type Component.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_product": "wallet_product",
    }

    def __init__(
        self,
        wallet_product=None,
        additional_properties=None):
        """Initialize a WalletProductResponse instance."""
        # Initialize members of the class
        self.wallet_product = wallet_product

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
        wallet_product =\
            Component.from_dictionary(
                dictionary.get("wallet_product"))\
                if dictionary.get("wallet_product") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_product,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_product=self.wallet_product
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_product={_wallet_product!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_product=self.wallet_product
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_product={_wallet_product!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
