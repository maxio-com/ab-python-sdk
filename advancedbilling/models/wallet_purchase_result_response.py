"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.wallet_purchase import (
    WalletPurchase,
)


class WalletPurchaseResultResponse(object):
    """Implementation of the 'Wallet Purchase Result Response' model.

    Attributes:
        wallet_purchases (List[WalletPurchase]): The model property of type
            List[WalletPurchase].
        balance (str): The wallet's new balance, as a decimal string.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_purchases": "wallet_purchases",
        "balance": "balance",
    }

    def __init__(
        self,
        wallet_purchases=None,
        balance=None,
        additional_properties=None):
        """Initialize a WalletPurchaseResultResponse instance."""
        # Initialize members of the class
        self.wallet_purchases = wallet_purchases
        self.balance = balance

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
        wallet_purchases = None
        if dictionary.get("wallet_purchases") is not None:
            wallet_purchases = [
                WalletPurchase.from_dictionary(x)
                    for x in dictionary.get("wallet_purchases")
            ]
        balance =\
            dictionary.get("balance")\
            if dictionary.get("balance")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_purchases,
                   balance,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_purchases=self.wallet_purchases
        _balance=self.balance
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_purchases={_wallet_purchases!r}, "
            f"balance={_balance!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_purchases=self.wallet_purchases
        _balance=self.balance
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_purchases={_wallet_purchases!s}, "
            f"balance={_balance!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
