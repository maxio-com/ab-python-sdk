"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class WalletTransaction(object):
    """Implementation of the 'Wallet Transaction' model.

    One append-only row on the wallet's ledger. Always appears bare inside a
    `wallet_transactions` array, never wrapped in its own key.

    Attributes:
        id (int): The Advanced Billing id of the ledger row.
        wallet_id (int): The model property of type int.
        kind (str): The kind of ledger row. Known values: `grant`, `debit`,
            `adjustment`, `initial_balance`, and `expiration`. More kinds are
            expected over time, so treat this as an open string and don't fail on one
            you don't recognize. Only `grant` and `debit` are accepted on [Create
            Wallet Transaction]($e/Wallet%20Transactions/createWalletTransaction).
            `adjustment` rows are written by [Create Wallet
            Adjustment]($e/Wallet%20Adjustments/createWalletAdjustment),
            `initial_balance` rows only by a seeded [Create
            Wallet]($e/Wallets/createWallet), and `expiration` rows only by the
            automatic expiry sweep that writes off an unconsumed grant once its
            `expires_at` passes.
        amount (str): A decimal string, **signed** on this resource. Non-negative for
            grants, negative for debits and expirations, either sign for adjustments.
            A grant row written after an overdraft repayment carries only what was
            left after the repayment (possibly `"0.0"`), not the grant's `original`.
        grant_id (int): The grant this row is attributed to. `null` for an overdraft
            row (a `kind: debit` row draining the below-zero portion of a balance,
            attributed to no grant), for an overdraft-repayment row (the `kind:
            grant` row that pays an existing negative balance back to zero, written
            before any remainder becomes a new grant), and for an overdraft
            correction (a `kind: adjustment` row posted against an overdraft entry,
            which credits no grant).
        source_transaction_id (int): For an `adjustment` row posted against a
            specific usage entry, the id of the `debit` row it corrects. `null` for
            every other kind, and for adjustments made against a grant's balance
            directly.
        source_corrections_total (str): For a `debit` row only, the signed sum (as a
            decimal string) of every adjustment posted against it so far (`"0.0"`
            when none). `null` for every other kind. The row's own `amount` is never
            rewritten, so a caller deriving the entry's corrected quantity nets this
            out of `amount`, and sends this value back as
            `expected_source_corrections` on a further correction.
        balance_after (str): The wallet's posted balance immediately after this row
            was applied, as a decimal string. Compare it with the wallet's
            `posted_balance`, not its `balance`.
        metered_from_at (datetime): For a row that closed a metered usage window (an
            hourly close, a depletion, or an expiry write-off), the start of that
            window. `null` on every other row.
        metered_through_at (datetime): The end of the usage window this row closed.
            `null` on every other row.
        conversion_rate_applied (str): The meter-to-wallet-unit conversion rate
            applied to compute this row's `amount`, as a decimal string. `null` on
            every other row.
        invoice_uid (str): The uid of the invoice behind a purchase's rows: the
            grant-creating row and, when the purchase repaid an overdraft, the
            repayment row. `null` on every other row.
        memo (str): Free-text note. For an `adjustment` row, carries the required
            `reason`.
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "wallet_id": "wallet_id",
        "kind": "kind",
        "amount": "amount",
        "grant_id": "grant_id",
        "source_transaction_id": "source_transaction_id",
        "source_corrections_total": "source_corrections_total",
        "balance_after": "balance_after",
        "metered_from_at": "metered_from_at",
        "metered_through_at": "metered_through_at",
        "conversion_rate_applied": "conversion_rate_applied",
        "invoice_uid": "invoice_uid",
        "memo": "memo",
        "created_at": "created_at",
    }

    _optionals = [
        "id",
        "wallet_id",
        "kind",
        "amount",
        "grant_id",
        "source_transaction_id",
        "source_corrections_total",
        "balance_after",
        "metered_from_at",
        "metered_through_at",
        "conversion_rate_applied",
        "invoice_uid",
        "memo",
        "created_at",
    ]

    _nullables = [
        "grant_id",
        "source_transaction_id",
        "source_corrections_total",
        "metered_from_at",
        "metered_through_at",
        "conversion_rate_applied",
        "invoice_uid",
        "memo",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        wallet_id=APIHelper.SKIP,
        kind=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        grant_id=APIHelper.SKIP,
        source_transaction_id=APIHelper.SKIP,
        source_corrections_total=APIHelper.SKIP,
        balance_after=APIHelper.SKIP,
        metered_from_at=APIHelper.SKIP,
        metered_through_at=APIHelper.SKIP,
        conversion_rate_applied=APIHelper.SKIP,
        invoice_uid=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletTransaction instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if wallet_id is not APIHelper.SKIP:
            self.wallet_id = wallet_id
        if kind is not APIHelper.SKIP:
            self.kind = kind
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if grant_id is not APIHelper.SKIP:
            self.grant_id = grant_id
        if source_transaction_id is not APIHelper.SKIP:
            self.source_transaction_id = source_transaction_id
        if source_corrections_total is not APIHelper.SKIP:
            self.source_corrections_total = source_corrections_total
        if balance_after is not APIHelper.SKIP:
            self.balance_after = balance_after
        if metered_from_at is not APIHelper.SKIP:
            self.metered_from_at =\
                 APIHelper.apply_datetime_converter(
                metered_from_at, APIHelper.RFC3339DateTime)\
                 if metered_from_at else None
        if metered_through_at is not APIHelper.SKIP:
            self.metered_through_at =\
                 APIHelper.apply_datetime_converter(
                metered_through_at, APIHelper.RFC3339DateTime)\
                 if metered_through_at else None
        if conversion_rate_applied is not APIHelper.SKIP:
            self.conversion_rate_applied = conversion_rate_applied
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        wallet_id =\
            dictionary.get("wallet_id")\
            if dictionary.get("wallet_id")\
                else APIHelper.SKIP
        kind =\
            dictionary.get("kind")\
            if dictionary.get("kind")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        grant_id =\
            dictionary.get("grant_id")\
            if "grant_id" in dictionary.keys()\
                else APIHelper.SKIP
        source_transaction_id =\
            dictionary.get("source_transaction_id")\
            if "source_transaction_id" in dictionary.keys()\
                else APIHelper.SKIP
        source_corrections_total =\
            dictionary.get("source_corrections_total")\
            if "source_corrections_total" in dictionary.keys()\
                else APIHelper.SKIP
        balance_after =\
            dictionary.get("balance_after")\
            if dictionary.get("balance_after")\
                else APIHelper.SKIP
        if "metered_from_at" in dictionary.keys():
            metered_from_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("metered_from_at")).datetime\
                if dictionary.get("metered_from_at") else None

        else:
            metered_from_at = APIHelper.SKIP
        if "metered_through_at" in dictionary.keys():
            metered_through_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("metered_through_at")).datetime\
                if dictionary.get("metered_through_at") else None

        else:
            metered_through_at = APIHelper.SKIP
        conversion_rate_applied =\
            dictionary.get("conversion_rate_applied")\
            if "conversion_rate_applied" in dictionary.keys()\
                else APIHelper.SKIP
        invoice_uid =\
            dictionary.get("invoice_uid")\
            if "invoice_uid" in dictionary.keys()\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if "memo" in dictionary.keys()\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   wallet_id,
                   kind,
                   amount,
                   grant_id,
                   source_transaction_id,
                   source_corrections_total,
                   balance_after,
                   metered_from_at,
                   metered_through_at,
                   conversion_rate_applied,
                   invoice_uid,
                   memo,
                   created_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _wallet_id=(
            self.wallet_id
            if hasattr(self, "wallet_id")
            else None
        )
        _kind=(
            self.kind
            if hasattr(self, "kind")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _grant_id=(
            self.grant_id
            if hasattr(self, "grant_id")
            else None
        )
        _source_transaction_id=(
            self.source_transaction_id
            if hasattr(self, "source_transaction_id")
            else None
        )
        _source_corrections_total=(
            self.source_corrections_total
            if hasattr(self, "source_corrections_total")
            else None
        )
        _balance_after=(
            self.balance_after
            if hasattr(self, "balance_after")
            else None
        )
        _metered_from_at=(
            self.metered_from_at
            if hasattr(self, "metered_from_at")
            else None
        )
        _metered_through_at=(
            self.metered_through_at
            if hasattr(self, "metered_through_at")
            else None
        )
        _conversion_rate_applied=(
            self.conversion_rate_applied
            if hasattr(self, "conversion_rate_applied")
            else None
        )
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"wallet_id={_wallet_id!r}, "
            f"kind={_kind!r}, "
            f"amount={_amount!r}, "
            f"grant_id={_grant_id!r}, "
            f"source_transaction_id={_source_transaction_id!r}, "
            f"source_corrections_total={_source_corrections_total!r}, "
            f"balance_after={_balance_after!r}, "
            f"metered_from_at={_metered_from_at!r}, "
            f"metered_through_at={_metered_through_at!r}, "
            f"conversion_rate_applied={_conversion_rate_applied!r}, "
            f"invoice_uid={_invoice_uid!r}, "
            f"memo={_memo!r}, "
            f"created_at={_created_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _wallet_id=(
            self.wallet_id
            if hasattr(self, "wallet_id")
            else None
        )
        _kind=(
            self.kind
            if hasattr(self, "kind")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _grant_id=(
            self.grant_id
            if hasattr(self, "grant_id")
            else None
        )
        _source_transaction_id=(
            self.source_transaction_id
            if hasattr(self, "source_transaction_id")
            else None
        )
        _source_corrections_total=(
            self.source_corrections_total
            if hasattr(self, "source_corrections_total")
            else None
        )
        _balance_after=(
            self.balance_after
            if hasattr(self, "balance_after")
            else None
        )
        _metered_from_at=(
            self.metered_from_at
            if hasattr(self, "metered_from_at")
            else None
        )
        _metered_through_at=(
            self.metered_through_at
            if hasattr(self, "metered_through_at")
            else None
        )
        _conversion_rate_applied=(
            self.conversion_rate_applied
            if hasattr(self, "conversion_rate_applied")
            else None
        )
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"wallet_id={_wallet_id!s}, "
            f"kind={_kind!s}, "
            f"amount={_amount!s}, "
            f"grant_id={_grant_id!s}, "
            f"source_transaction_id={_source_transaction_id!s}, "
            f"source_corrections_total={_source_corrections_total!s}, "
            f"balance_after={_balance_after!s}, "
            f"metered_from_at={_metered_from_at!s}, "
            f"metered_through_at={_metered_through_at!s}, "
            f"conversion_rate_applied={_conversion_rate_applied!s}, "
            f"invoice_uid={_invoice_uid!s}, "
            f"memo={_memo!s}, "
            f"created_at={_created_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
