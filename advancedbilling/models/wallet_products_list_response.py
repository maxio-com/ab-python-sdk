"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.wallet_product_list_item import (
    WalletProductListItem,
)


class WalletProductsListResponse(object):
    """Implementation of the 'Wallet Products List Response' model.

    Attributes:
        wallet_products (List[WalletProductListItem]): The model property of type
            List[WalletProductListItem].
        total_count (int): Total number of Wallet Products matching the filters,
            across all pages.
        archived_count (int): Not a simple count of archived products matching the
            filters. With `status=archived`, equals `total_count` (there's nothing
            else to report). With any other `status`, it's `0` whenever `total_count`
            is non-zero, and only when `total_count` is `0` does it become the number
            of archived Wallet Products matching the same `q` search term (ignoring
            `status`): an empty-state hint, not a running total.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_products": "wallet_products",
        "total_count": "total_count",
        "archived_count": "archived_count",
    }

    def __init__(
        self,
        wallet_products=None,
        total_count=None,
        archived_count=None,
        additional_properties=None):
        """Initialize a WalletProductsListResponse instance."""
        # Initialize members of the class
        self.wallet_products = wallet_products
        self.total_count = total_count
        self.archived_count = archived_count

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
        wallet_products = None
        if dictionary.get("wallet_products") is not None:
            wallet_products = [
                WalletProductListItem.from_dictionary(x)
                    for x in dictionary.get("wallet_products")
            ]
        total_count =\
            dictionary.get("total_count")\
            if dictionary.get("total_count")\
                else None
        archived_count =\
            dictionary.get("archived_count")\
            if dictionary.get("archived_count")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_products,
                   total_count,
                   archived_count,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_products=self.wallet_products
        _total_count=self.total_count
        _archived_count=self.archived_count
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_products={_wallet_products!r}, "
            f"total_count={_total_count!r}, "
            f"archived_count={_archived_count!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_products=self.wallet_products
        _total_count=self.total_count
        _archived_count=self.archived_count
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_products={_wallet_products!s}, "
            f"total_count={_total_count!s}, "
            f"archived_count={_archived_count!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
