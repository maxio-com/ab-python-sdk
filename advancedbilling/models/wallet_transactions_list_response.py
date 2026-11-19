"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.list_public_keys_meta import (
    ListPublicKeysMeta,
)
from advancedbilling.models.wallet_transaction import (
    WalletTransaction,
)


class WalletTransactionsListResponse(object):
    """Implementation of the 'Wallet Transactions List Response' model.

    Attributes:
        wallet_transactions (List[WalletTransaction]): The model property of type
            List[WalletTransaction].
        meta (ListPublicKeysMeta): The model property of type ListPublicKeysMeta.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_transactions": "wallet_transactions",
        "meta": "meta",
    }

    def __init__(
        self,
        wallet_transactions=None,
        meta=None,
        additional_properties=None):
        """Initialize a WalletTransactionsListResponse instance."""
        # Initialize members of the class
        self.wallet_transactions = wallet_transactions
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
        wallet_transactions = None
        if dictionary.get("wallet_transactions") is not None:
            wallet_transactions = [
                WalletTransaction.from_dictionary(x)
                    for x in dictionary.get("wallet_transactions")
            ]
        meta =\
            ListPublicKeysMeta.from_dictionary(
                dictionary.get("meta"))\
                if dictionary.get("meta") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_transactions,
                   meta,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_transactions=self.wallet_transactions
        _meta=self.meta
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_transactions={_wallet_transactions!r}, "
            f"meta={_meta!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_transactions=self.wallet_transactions
        _meta=self.meta
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_transactions={_wallet_transactions!s}, "
            f"meta={_meta!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
