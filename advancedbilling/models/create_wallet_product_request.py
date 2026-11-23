"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.wallet_product import (
    WalletProduct,
)


class CreateWalletProductRequest(object):
    """Implementation of the 'Create Wallet Product Request' model.

    Does not accept `product_family_id`: a Wallet Product never belongs to a product
    family. The underlying endpoint accepts the param, but only to reject it; sending
    one returns `422` ("Product family cannot be set on a wallet product") rather
    than silently ignoring it.

    Attributes:
        wallet_product (WalletProduct): The model property of type WalletProduct.
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
        """Initialize a CreateWalletProductRequest instance."""
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
            WalletProduct.from_dictionary(
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
