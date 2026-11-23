"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.wallet_product_1 import (
    WalletProduct1,
)


class UpdateWalletProductRequest(object):
    """Implementation of the 'Update Wallet Product Request' model.

    Only `name`, `description`, `taxable`, `tax_code`, `accounting_code`, and
    `item_category` are mutable. `unit_name`, `handle`, `price_point`, and
    `price_points` are not accepted here: the request still returns `200`, but those
    fields are silently ignored and nothing about them changes. `handle` stays fixed
    because it's the Wallet Product's only stable identifier on a surface with no
    product family in the path; `unit_name` stays fixed because a wallet's behavior
    snapshots it into the wallet's own `unit` field and never re-derives it.

    Attributes:
        wallet_product (WalletProduct1): The model property of type WalletProduct1.
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
        """Initialize a UpdateWalletProductRequest instance."""
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
            WalletProduct1.from_dictionary(
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
