"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.wallet_transaction import (
    WalletTransaction,
)


class WalletTransactionResultResponse(object):
    """Implementation of the 'Wallet Transaction Result Response' model.

    Returned by [Create Wallet
    Transaction]($e/Wallet%20Transactions/createWalletTransaction).
    `wallet_transactions` and `balance` are always present. `requested_amount`,
    `drained_amount`, and `rejected_amount` are present only when the request's
    `kind` was `debit`.

    Attributes:
        wallet_transactions (List[WalletTransaction]): The model property of type
            List[WalletTransaction].
        requested_amount (str): `kind: debit` only. The amount that was requested, as
            a decimal string.
        drained_amount (str): `kind: debit` only. The amount actually drained from
            the wallet's grants, as a decimal string.
        rejected_amount (str): `kind: debit` only, as a decimal string. Under
            `hard_stop_overflow: discard`, this is the requested amount minus what
            the wallet could cover (`"0.0"` on a full drain). Always `"0.0"` under
            `allow_negative`; nothing is rejected, and the balance goes negative
            instead.
        balance (str): The wallet's new balance, as a decimal string.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_transactions": "wallet_transactions",
        "balance": "balance",
        "requested_amount": "requested_amount",
        "drained_amount": "drained_amount",
        "rejected_amount": "rejected_amount",
    }

    _optionals = [
        "requested_amount",
        "drained_amount",
        "rejected_amount",
    ]

    def __init__(
        self,
        wallet_transactions=None,
        balance=None,
        requested_amount=APIHelper.SKIP,
        drained_amount=APIHelper.SKIP,
        rejected_amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletTransactionResultResponse instance."""
        # Initialize members of the class
        self.wallet_transactions = wallet_transactions
        if requested_amount is not APIHelper.SKIP:
            self.requested_amount = requested_amount
        if drained_amount is not APIHelper.SKIP:
            self.drained_amount = drained_amount
        if rejected_amount is not APIHelper.SKIP:
            self.rejected_amount = rejected_amount
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
        wallet_transactions = None
        if dictionary.get("wallet_transactions") is not None:
            wallet_transactions = [
                WalletTransaction.from_dictionary(x)
                    for x in dictionary.get("wallet_transactions")
            ]
        balance =\
            dictionary.get("balance")\
            if dictionary.get("balance")\
                else None
        requested_amount =\
            dictionary.get("requested_amount")\
            if dictionary.get("requested_amount")\
                else APIHelper.SKIP
        drained_amount =\
            dictionary.get("drained_amount")\
            if dictionary.get("drained_amount")\
                else APIHelper.SKIP
        rejected_amount =\
            dictionary.get("rejected_amount")\
            if dictionary.get("rejected_amount")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_transactions,
                   balance,
                   requested_amount,
                   drained_amount,
                   rejected_amount,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_transactions=self.wallet_transactions
        _requested_amount=(
            self.requested_amount
            if hasattr(self, "requested_amount")
            else None
        )
        _drained_amount=(
            self.drained_amount
            if hasattr(self, "drained_amount")
            else None
        )
        _rejected_amount=(
            self.rejected_amount
            if hasattr(self, "rejected_amount")
            else None
        )
        _balance=self.balance
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_transactions={_wallet_transactions!r}, "
            f"requested_amount={_requested_amount!r}, "
            f"drained_amount={_drained_amount!r}, "
            f"rejected_amount={_rejected_amount!r}, "
            f"balance={_balance!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_transactions=self.wallet_transactions
        _requested_amount=(
            self.requested_amount
            if hasattr(self, "requested_amount")
            else None
        )
        _drained_amount=(
            self.drained_amount
            if hasattr(self, "drained_amount")
            else None
        )
        _rejected_amount=(
            self.rejected_amount
            if hasattr(self, "rejected_amount")
            else None
        )
        _balance=self.balance
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_transactions={_wallet_transactions!s}, "
            f"requested_amount={_requested_amount!s}, "
            f"drained_amount={_drained_amount!s}, "
            f"rejected_amount={_rejected_amount!s}, "
            f"balance={_balance!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
