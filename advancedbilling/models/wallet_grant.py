"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class WalletGrant(object):
    """Implementation of the 'Wallet Grant' model.

    A funding tranche embedded on the wallet. `original` is the amount the grant was
    created with; `posted_remaining` is what debits and adjustments written to the
    ledger have left; `remaining` is what can still be spent. Debits drain grants
    earliest-expiration-first (grants with no expiration are drained last).

    Attributes:
        id (int): The Advanced Billing id of the grant.
        name (str): The memo the grant was created with, or `Grant
        original (str): The amount the grant was created with, encoded as a decimal
            string. Never changes after creation.
        remaining (str): What the grant can still spend, encoded as a decimal string.
            On [Read Wallet]($e/Wallets/readWallet) for a metered wallet whose
            `balance` is the live figure, this is `posted_remaining` less the pending
            usage drawn from this grant in drain order: usage past a grant spills to
            the next one, and usage past every grant is an overdraft that belongs to
            no grant. It never goes below zero, and the grants' `remaining` add up to
            the wallet's `balance` whenever `balance` is zero or more. Everywhere
            else it equals `posted_remaining`.
        posted_remaining (str): The grant's remainder from written ledger entries
            alone, encoded as a decimal string. Always present. This is the figure an
            adjustment checks `expected_remaining` and its bounds against, so send it
            back, not `remaining`, when correcting a grant.
        expires_at (datetime): When this grant's unconsumed remainder is
            automatically written off. `null` for an evergreen grant.
        expires_on (date): The calendar day `expires_at` falls on, already resolved
            in the site's time zone.
        expired_at (datetime): When the expiry sweep actually wrote this grant's
            remainder off. Usually falls shortly after `expires_at`; use `expires_on`
            for the date the grant expired, not this field. `null` if the grant was
            never written off (including a grant simply spent to zero before its
            `expires_at`).
        expired_on (date): The calendar day `expired_at` falls on, resolved in the
            site's time zone.
        origin (Origin): How the grant was created. `recurring` comes from the
            wallet's automatic funding schedule (see the wallet's `recurring_funding`
            array). `manual` comes from a one-time grant posted to [Create Wallet
            Transaction]($e/Wallet%20Transactions/createWalletTransaction).
            `initial_balance` comes from a non-zero `initial_balance` at wallet
            creation. `allowance_increase` comes from raising a funding entitlement's
            allowance while it's already funding a wallet. `purchase` comes from
            [Create Wallet Purchase]($e/Wallet%20Purchases/createWalletPurchase).
        granted_for_period_start (datetime): For a `recurring` grant, the start of
            the funding cadence period this grant covers. `null` for every other
            origin. After a gap in funding (see `skipped_periods`), this is the
            period currently in progress, not the oldest period that was missed.
        invoice_uid (str): The uid of the invoice that paid for this grant, for a
            grant with `origin` of `purchase`. `null` for every other origin.
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "name": "name",
        "original": "original",
        "remaining": "remaining",
        "posted_remaining": "posted_remaining",
        "expires_at": "expires_at",
        "expires_on": "expires_on",
        "expired_at": "expired_at",
        "expired_on": "expired_on",
        "origin": "origin",
        "granted_for_period_start": "granted_for_period_start",
        "invoice_uid": "invoice_uid",
        "created_at": "created_at",
    }

    _optionals = [
        "id",
        "name",
        "original",
        "remaining",
        "posted_remaining",
        "expires_at",
        "expires_on",
        "expired_at",
        "expired_on",
        "origin",
        "granted_for_period_start",
        "invoice_uid",
        "created_at",
    ]

    _nullables = [
        "expires_at",
        "expires_on",
        "expired_at",
        "expired_on",
        "granted_for_period_start",
        "invoice_uid",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        original=APIHelper.SKIP,
        remaining=APIHelper.SKIP,
        posted_remaining=APIHelper.SKIP,
        expires_at=APIHelper.SKIP,
        expires_on=APIHelper.SKIP,
        expired_at=APIHelper.SKIP,
        expired_on=APIHelper.SKIP,
        origin=APIHelper.SKIP,
        granted_for_period_start=APIHelper.SKIP,
        invoice_uid=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletGrant instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if original is not APIHelper.SKIP:
            self.original = original
        if remaining is not APIHelper.SKIP:
            self.remaining = remaining
        if posted_remaining is not APIHelper.SKIP:
            self.posted_remaining = posted_remaining
        if expires_at is not APIHelper.SKIP:
            self.expires_at =\
                 APIHelper.apply_datetime_converter(
                expires_at, APIHelper.RFC3339DateTime)\
                 if expires_at else None
        if expires_on is not APIHelper.SKIP:
            self.expires_on = expires_on
        if expired_at is not APIHelper.SKIP:
            self.expired_at =\
                 APIHelper.apply_datetime_converter(
                expired_at, APIHelper.RFC3339DateTime)\
                 if expired_at else None
        if expired_on is not APIHelper.SKIP:
            self.expired_on = expired_on
        if origin is not APIHelper.SKIP:
            self.origin = origin
        if granted_for_period_start is not APIHelper.SKIP:
            self.granted_for_period_start =\
                 APIHelper.apply_datetime_converter(
                granted_for_period_start, APIHelper.RFC3339DateTime)\
                 if granted_for_period_start else None
        if invoice_uid is not APIHelper.SKIP:
            self.invoice_uid = invoice_uid
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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        original =\
            dictionary.get("original")\
            if dictionary.get("original")\
                else APIHelper.SKIP
        remaining =\
            dictionary.get("remaining")\
            if dictionary.get("remaining")\
                else APIHelper.SKIP
        posted_remaining =\
            dictionary.get("posted_remaining")\
            if dictionary.get("posted_remaining")\
                else APIHelper.SKIP
        if "expires_at" in dictionary.keys():
            expires_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("expires_at")).datetime\
                if dictionary.get("expires_at") else None

        else:
            expires_at = APIHelper.SKIP
        if "expires_on" in dictionary.keys():
            expires_on = dateutil.parser.parse(
                dictionary.get("expires_on")).date()\
                if dictionary.get("expires_on") else None

        else:
            expires_on = APIHelper.SKIP
        if "expired_at" in dictionary.keys():
            expired_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("expired_at")).datetime\
                if dictionary.get("expired_at") else None

        else:
            expired_at = APIHelper.SKIP
        if "expired_on" in dictionary.keys():
            expired_on = dateutil.parser.parse(
                dictionary.get("expired_on")).date()\
                if dictionary.get("expired_on") else None

        else:
            expired_on = APIHelper.SKIP
        origin =\
            dictionary.get("origin")\
            if dictionary.get("origin")\
                else APIHelper.SKIP
        if "granted_for_period_start" in dictionary.keys():
            granted_for_period_start = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("granted_for_period_start")).datetime\
                if dictionary.get("granted_for_period_start") else None

        else:
            granted_for_period_start = APIHelper.SKIP
        invoice_uid =\
            dictionary.get("invoice_uid")\
            if "invoice_uid" in dictionary.keys()\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   name,
                   original,
                   remaining,
                   posted_remaining,
                   expires_at,
                   expires_on,
                   expired_at,
                   expired_on,
                   origin,
                   granted_for_period_start,
                   invoice_uid,
                   created_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _original=(
            self.original
            if hasattr(self, "original")
            else None
        )
        _remaining=(
            self.remaining
            if hasattr(self, "remaining")
            else None
        )
        _posted_remaining=(
            self.posted_remaining
            if hasattr(self, "posted_remaining")
            else None
        )
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _expires_on=(
            self.expires_on
            if hasattr(self, "expires_on")
            else None
        )
        _expired_at=(
            self.expired_at
            if hasattr(self, "expired_at")
            else None
        )
        _expired_on=(
            self.expired_on
            if hasattr(self, "expired_on")
            else None
        )
        _origin=(
            self.origin
            if hasattr(self, "origin")
            else None
        )
        _granted_for_period_start=(
            self.granted_for_period_start
            if hasattr(self, "granted_for_period_start")
            else None
        )
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
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
            f"name={_name!r}, "
            f"original={_original!r}, "
            f"remaining={_remaining!r}, "
            f"posted_remaining={_posted_remaining!r}, "
            f"expires_at={_expires_at!r}, "
            f"expires_on={_expires_on!r}, "
            f"expired_at={_expired_at!r}, "
            f"expired_on={_expired_on!r}, "
            f"origin={_origin!r}, "
            f"granted_for_period_start={_granted_for_period_start!r}, "
            f"invoice_uid={_invoice_uid!r}, "
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _original=(
            self.original
            if hasattr(self, "original")
            else None
        )
        _remaining=(
            self.remaining
            if hasattr(self, "remaining")
            else None
        )
        _posted_remaining=(
            self.posted_remaining
            if hasattr(self, "posted_remaining")
            else None
        )
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _expires_on=(
            self.expires_on
            if hasattr(self, "expires_on")
            else None
        )
        _expired_at=(
            self.expired_at
            if hasattr(self, "expired_at")
            else None
        )
        _expired_on=(
            self.expired_on
            if hasattr(self, "expired_on")
            else None
        )
        _origin=(
            self.origin
            if hasattr(self, "origin")
            else None
        )
        _granted_for_period_start=(
            self.granted_for_period_start
            if hasattr(self, "granted_for_period_start")
            else None
        )
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
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
            f"name={_name!s}, "
            f"original={_original!s}, "
            f"remaining={_remaining!s}, "
            f"posted_remaining={_posted_remaining!s}, "
            f"expires_at={_expires_at!s}, "
            f"expires_on={_expires_on!s}, "
            f"expired_at={_expired_at!s}, "
            f"expired_on={_expired_on!s}, "
            f"origin={_origin!s}, "
            f"granted_for_period_start={_granted_for_period_start!s}, "
            f"invoice_uid={_invoice_uid!s}, "
            f"created_at={_created_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
