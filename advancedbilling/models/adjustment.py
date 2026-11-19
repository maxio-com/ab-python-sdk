"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Adjustment(object):
    """Implementation of the 'Adjustment' model.

    Attributes:
        amount (str | int): Signed: positive adds units to the grant, negative
            removes them. Bounded below by the grant's `posted_remaining` (a
            correction can't drive it negative) and above by the grant's `original`
            (a correction can't credit past what was originally granted). An
            out-of-bounds value is rejected rather than clamped. Zero is rejected.
            Without a `grant_id` (an overdraft correction), the amount must be
            positive, can't exceed the usage the overdraft entry still records, and
            can't exceed the overdraft the wallet still owes. Encoded as a decimal
            string with at most 8 fractional digits. Send fractional values as
            strings: a JSON number with a decimal point is rejected with `422`,
            because a double-precision float may already have lost precision before
            the request arrives.
        reason (str): Required. Lands on the resulting ledger row's `memo`.
        grant_id (int): The grant to correct. Must belong to this wallet. Required
            unless `source_transaction_id` names an overdraft entry (a `debit` with
            no `grant_id`, written when an `allow_negative` wallet consumes past its
            grants). For an overdraft entry, omit it: sending one returns `422`, and
            the correction credits the wallet's outstanding overdraft instead of any
            grant.
        source_transaction_id (int): (Optional) The `debit` row this correction is
            fixing. Must belong to this wallet, and must name a row of kind `debit`;
            grant and adjustment rows are append-only history, corrected by posting a
            further adjustment rather than by pointing at them. For a
            grant-attributed debit, it's recorded on the resulting ledger row for
            audit only: it does not change how `amount` is applied, and more than one
            adjustment may name the same row. For an overdraft entry, it decides the
            path: omit `grant_id`, and the correction is credit-only, bounded by the
            usage the entry still records and by the overdraft the wallet still owes.
        expected_remaining (str): (Optional) An optimistic-concurrency check for a
            caller whose `amount` was derived from the grant's own remainder. Send
            the grant's `posted_remaining`, not its `remaining`: on a metered wallet
            read through [Read Wallet]($e/Wallets/readWallet), `remaining` also
            subtracts usage not yet posted, so it can differ from what the adjustment
            checks. If given and the grant's current `posted_remaining` no longer
            matches, the request is rejected with `409` and nothing is written.
            Compared numerically, so `"100"` and `"100.00000000"` both match a
            `posted_remaining` of `100`. Omit the field entirely to skip the check;
            sending it as an empty string is treated as a malformed value (`422`),
            not as an omission.
        expected_source_corrections (str): (Optional) An optimistic-concurrency check
            for a caller whose `amount` was derived from a usage entry, sent together
            with `source_transaction_id`: the entry's `source_corrections_total` as
            the caller last read it (`"0"` if none). If the sum the server computes
            no longer matches, the request is rejected with `409` and nothing is
            written. This is what catches a correction posted between that read and
            this request. Ignored unless `source_transaction_id` is also given.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "reason": "reason",
        "grant_id": "grant_id",
        "source_transaction_id": "source_transaction_id",
        "expected_remaining": "expected_remaining",
        "expected_source_corrections": "expected_source_corrections",
    }

    _optionals = [
        "grant_id",
        "source_transaction_id",
        "expected_remaining",
        "expected_source_corrections",
    ]

    _nullables = [
        "grant_id",
        "source_transaction_id",
        "expected_remaining",
        "expected_source_corrections",
    ]

    def __init__(
        self,
        amount=None,
        reason=None,
        grant_id=APIHelper.SKIP,
        source_transaction_id=APIHelper.SKIP,
        expected_remaining=APIHelper.SKIP,
        expected_source_corrections=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Adjustment instance."""
        # Initialize members of the class
        self.amount = amount
        self.reason = reason
        if grant_id is not APIHelper.SKIP:
            self.grant_id = grant_id
        if source_transaction_id is not APIHelper.SKIP:
            self.source_transaction_id = source_transaction_id
        if expected_remaining is not APIHelper.SKIP:
            self.expected_remaining = expected_remaining
        if expected_source_corrections is not APIHelper.SKIP:
            self.expected_source_corrections = expected_source_corrections

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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        amount = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("AdjustmentAmount"),
            dictionary.get("amount"),
            False)\
            if dictionary.get("amount") is not None\
            else None
        reason =\
            dictionary.get("reason")\
            if dictionary.get("reason")\
                else None
        grant_id =\
            dictionary.get("grant_id")\
            if "grant_id" in dictionary.keys()\
                else APIHelper.SKIP
        source_transaction_id =\
            dictionary.get("source_transaction_id")\
            if "source_transaction_id" in dictionary.keys()\
                else APIHelper.SKIP
        expected_remaining =\
            dictionary.get("expected_remaining")\
            if "expected_remaining" in dictionary.keys()\
                else APIHelper.SKIP
        expected_source_corrections =\
            dictionary.get("expected_source_corrections")\
            if "expected_source_corrections" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(amount,
                   reason,
                   grant_id,
                   source_transaction_id,
                   expected_remaining,
                   expected_source_corrections,
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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if isinstance(dictionary, cls):
            return (UnionTypeLookUp.get("AdjustmentAmount")
                .validate(dictionary.amount).is_valid) \
                and APIHelper.is_valid_type(
                    value=dictionary.reason,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return (UnionTypeLookUp.get("AdjustmentAmount")
            .validate(dictionary.get("amount")).is_valid) \
            and APIHelper.is_valid_type(
                value=dictionary.get("reason"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _amount=self.amount
        _reason=self.reason
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
        _expected_remaining=(
            self.expected_remaining
            if hasattr(self, "expected_remaining")
            else None
        )
        _expected_source_corrections=(
            self.expected_source_corrections
            if hasattr(self, "expected_source_corrections")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!r}, "
            f"reason={_reason!r}, "
            f"grant_id={_grant_id!r}, "
            f"source_transaction_id={_source_transaction_id!r}, "
            f"expected_remaining={_expected_remaining!r}, "
            f"expected_source_corrections={_expected_source_corrections!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _amount=self.amount
        _reason=self.reason
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
        _expected_remaining=(
            self.expected_remaining
            if hasattr(self, "expected_remaining")
            else None
        )
        _expected_source_corrections=(
            self.expected_source_corrections
            if hasattr(self, "expected_source_corrections")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!s}, "
            f"reason={_reason!s}, "
            f"grant_id={_grant_id!s}, "
            f"source_transaction_id={_source_transaction_id!s}, "
            f"expected_remaining={_expected_remaining!s}, "
            f"expected_source_corrections={_expected_source_corrections!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
