"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.meter import Meter
from advancedbilling.models.wallet_grant import (
    WalletGrant,
)
from advancedbilling.models.wallet_recurring_funding import (
    WalletRecurringFunding,
)


class Wallet(object):
    """Implementation of the 'Wallet' model.

    A balance, denominated in the unit of a Wallet Product, owned by a subscription.
    Grants and recurring funding schedules are embedded so a single read shows the
    full balance breakdown.

    Attributes:
        id (int): The Advanced Billing id of the wallet.
        owner_type (OwnerType): The polymorphic owner type. `subscription` is the
            only value currently supported.
        owner_id (int): The id of the owning subscription.
        name (str): (Optional) A merchant-facing label for the wallet, set on create
            and changeable with [Update Wallet]($e/Wallets/updateWallet). Surrounding
            spaces are stripped; a blank value is stored as `null`.
        wallet_product_id (int): The id of the [Wallet
            Product]($e/Wallet%20Products/createWalletProduct) that denominates the
            wallet. Immutable for the life of the wallet.
        wallet_product_name (str): The name of the Wallet Product that denominates
            the wallet.
        unit (str): The billing product's unit name, immutable for the life of the
            wallet.
        price_point_id (int): The price point that priced this wallet's
            [purchases]($e/Wallet%20Purchases/createWalletPurchase), set on create
            and immutable afterward. Defaults to the Wallet Product's default price
            point; `null` if the Wallet Product has none and none was given on create.
        balance (str): What the wallet can spend now, encoded as a decimal string to
            avoid floating-point precision loss. This is the number to enforce
            against. For a metered wallet, it includes usage not yet posted to the
            ledger, through `metered_through_at`, but only in the response from [Read
            Wallet]($e/Wallets/readWallet); every other response (list, create,
            update, archive) reports the balance as of the last ledger write, equal
            to `posted_balance`, even for a metered wallet. The grants' `remaining`
            follow this figure, so they add up to it whenever it is zero or more.
        posted_balance (str): The balance from written ledger entries alone: grants
            funded, minus debits written to the ledger, as a decimal string. Always
            present, also for a wallet with no meter. It equals `balance` wherever no
            live metered balance is computed: list, create, update, and archive
            responses, an unlinked or archived wallet, and a read where
            `metered_stale` is `true`. Only an active, metered wallet read through
            [Read Wallet]($e/Wallets/readWallet), with `metered_stale` not `true`,
            can have a `balance` below its `posted_balance`. It stays exact when
            `metered_stale` is `true`. Reconcile the transactions list
            (`balance_after`) against this figure, not against `balance`.
        meter (Meter): The metering meter this wallet is paired with, or `null` for a
            wallet with no meter. Set on create and immutable afterward.
        metered_through_at (datetime): The point up to which live meter usage has
            been factored into `balance`. Populated only in the response from [Read
            Wallet]($e/Wallets/readWallet), for an active, metered wallet on a site
            with metered consumption enabled; `null` everywhere else, including list,
            create, update, and archive responses for the same wallet.
        metered_recheck_after_seconds (int): How many seconds to wait before
            re-reading `balance` to see usage past `metered_through_at`. Same
            availability as `metered_through_at`.
        metered_stale (bool): `true` when live usage could not be read fresh and
            `balance` reflects an earlier snapshot. Same availability as
            `metered_through_at`.
        status (WalletStatus): The model property of type WalletStatus.
        depletion_policy (str): What happens when a debit would take the wallet below
            zero. Known values: `hard_stop` (the only value you can set today). More
            values are expected over time, so treat this as an open string and don't
            fail on one you don't recognize. At the zero boundary, `hard_stop`
            behaves as set by `hard_stop_overflow`.
        hard_stop_overflow (WalletHardStopOverflow): Behavior at the hard-stop
            boundary. `discard` drains the wallet to zero and rejects the excess (the
            default). `allow_negative` deducts the full amount, letting the balance
            go negative. The excess past the wallet's grants is booked as an
            overdraft ledger row with `grant_id` set to `null`.
        origin (WalletOrigin): How the wallet came to exist. `manual` for a wallet
            created directly with [Create Wallet]($e/Wallets/createWallet). `feature`
            for a wallet auto-provisioned because a subscription resolved a
            usage-limit entitlement whose Feature has `wallet_behavior` configured.
        feature_key (str): The key of the Feature this wallet was provisioned for,
            when `origin` is `feature`. `null` for a `manual` wallet.
        grants (List[WalletGrant]): Every grant on the wallet, including ones already
            spent or expired, in drain order (the order debits would consume the
            still-open ones in): the soonest-expiring grant first, evergreen grants
            last.
        recurring_funding (List[WalletRecurringFunding]): The wallet's automatic
            funding schedules, if any. Empty for a `manual` wallet with no funding
            entitlement. A wallet funds automatically when it's provisioned from a
            Feature with `wallet_behavior` configured; see [the Wallets concept
            guide](page:introduction/basic-concepts/wallets#provisioning-a-wallet-from
            -a-feature).
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "owner_type": "owner_type",
        "owner_id": "owner_id",
        "name": "name",
        "wallet_product_id": "wallet_product_id",
        "wallet_product_name": "wallet_product_name",
        "unit": "unit",
        "price_point_id": "price_point_id",
        "balance": "balance",
        "posted_balance": "posted_balance",
        "meter": "meter",
        "metered_through_at": "metered_through_at",
        "metered_recheck_after_seconds": "metered_recheck_after_seconds",
        "metered_stale": "metered_stale",
        "status": "status",
        "depletion_policy": "depletion_policy",
        "hard_stop_overflow": "hard_stop_overflow",
        "origin": "origin",
        "feature_key": "feature_key",
        "grants": "grants",
        "recurring_funding": "recurring_funding",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }

    _optionals = [
        "id",
        "owner_type",
        "owner_id",
        "name",
        "wallet_product_id",
        "wallet_product_name",
        "unit",
        "price_point_id",
        "balance",
        "posted_balance",
        "meter",
        "metered_through_at",
        "metered_recheck_after_seconds",
        "metered_stale",
        "status",
        "depletion_policy",
        "hard_stop_overflow",
        "origin",
        "feature_key",
        "grants",
        "recurring_funding",
        "created_at",
        "updated_at",
    ]

    _nullables = [
        "name",
        "price_point_id",
        "meter",
        "metered_through_at",
        "metered_recheck_after_seconds",
        "metered_stale",
        "feature_key",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        owner_type=APIHelper.SKIP,
        owner_id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        wallet_product_id=APIHelper.SKIP,
        wallet_product_name=APIHelper.SKIP,
        unit=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        balance=APIHelper.SKIP,
        posted_balance=APIHelper.SKIP,
        meter=APIHelper.SKIP,
        metered_through_at=APIHelper.SKIP,
        metered_recheck_after_seconds=APIHelper.SKIP,
        metered_stale=APIHelper.SKIP,
        status=APIHelper.SKIP,
        depletion_policy=APIHelper.SKIP,
        hard_stop_overflow=APIHelper.SKIP,
        origin=APIHelper.SKIP,
        feature_key=APIHelper.SKIP,
        grants=APIHelper.SKIP,
        recurring_funding=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        updated_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Wallet instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if owner_type is not APIHelper.SKIP:
            self.owner_type = owner_type
        if owner_id is not APIHelper.SKIP:
            self.owner_id = owner_id
        if name is not APIHelper.SKIP:
            self.name = name
        if wallet_product_id is not APIHelper.SKIP:
            self.wallet_product_id = wallet_product_id
        if wallet_product_name is not APIHelper.SKIP:
            self.wallet_product_name = wallet_product_name
        if unit is not APIHelper.SKIP:
            self.unit = unit
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if balance is not APIHelper.SKIP:
            self.balance = balance
        if posted_balance is not APIHelper.SKIP:
            self.posted_balance = posted_balance
        if meter is not APIHelper.SKIP:
            self.meter = meter
        if metered_through_at is not APIHelper.SKIP:
            self.metered_through_at =\
                 APIHelper.apply_datetime_converter(
                metered_through_at, APIHelper.RFC3339DateTime)\
                 if metered_through_at else None
        if metered_recheck_after_seconds is not APIHelper.SKIP:
            self.metered_recheck_after_seconds = metered_recheck_after_seconds
        if metered_stale is not APIHelper.SKIP:
            self.metered_stale = metered_stale
        if status is not APIHelper.SKIP:
            self.status = status
        if depletion_policy is not APIHelper.SKIP:
            self.depletion_policy = depletion_policy
        if hard_stop_overflow is not APIHelper.SKIP:
            self.hard_stop_overflow = hard_stop_overflow
        if origin is not APIHelper.SKIP:
            self.origin = origin
        if feature_key is not APIHelper.SKIP:
            self.feature_key = feature_key
        if grants is not APIHelper.SKIP:
            self.grants = grants
        if recurring_funding is not APIHelper.SKIP:
            self.recurring_funding = recurring_funding
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None
        if updated_at is not APIHelper.SKIP:
            self.updated_at =\
                 APIHelper.apply_datetime_converter(
                updated_at, APIHelper.RFC3339DateTime)\
                 if updated_at else None

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
        owner_type =\
            dictionary.get("owner_type")\
            if dictionary.get("owner_type")\
                else APIHelper.SKIP
        owner_id =\
            dictionary.get("owner_id")\
            if dictionary.get("owner_id")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if "name" in dictionary.keys()\
                else APIHelper.SKIP
        wallet_product_id =\
            dictionary.get("wallet_product_id")\
            if dictionary.get("wallet_product_id")\
                else APIHelper.SKIP
        wallet_product_name =\
            dictionary.get("wallet_product_name")\
            if dictionary.get("wallet_product_name")\
                else APIHelper.SKIP
        unit =\
            dictionary.get("unit")\
            if dictionary.get("unit")\
                else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if "price_point_id" in dictionary.keys()\
                else APIHelper.SKIP
        balance =\
            dictionary.get("balance")\
            if dictionary.get("balance")\
                else APIHelper.SKIP
        posted_balance =\
            dictionary.get("posted_balance")\
            if dictionary.get("posted_balance")\
                else APIHelper.SKIP
        if "meter" in dictionary.keys():
            meter =\
                Meter.from_dictionary(
                dictionary.get("meter"))\
                if dictionary.get("meter") else None
        else:
            meter = APIHelper.SKIP
        if "metered_through_at" in dictionary.keys():
            metered_through_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("metered_through_at")).datetime\
                if dictionary.get("metered_through_at") else None

        else:
            metered_through_at = APIHelper.SKIP
        metered_recheck_after_seconds =\
            dictionary.get("metered_recheck_after_seconds")\
            if "metered_recheck_after_seconds" in dictionary.keys()\
                else APIHelper.SKIP
        metered_stale =\
            dictionary.get("metered_stale")\
            if "metered_stale" in dictionary.keys()\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        depletion_policy =\
            dictionary.get("depletion_policy")\
            if dictionary.get("depletion_policy")\
                else APIHelper.SKIP
        hard_stop_overflow =\
            dictionary.get("hard_stop_overflow")\
            if dictionary.get("hard_stop_overflow")\
                else APIHelper.SKIP
        origin =\
            dictionary.get("origin")\
            if dictionary.get("origin")\
                else APIHelper.SKIP
        feature_key =\
            dictionary.get("feature_key")\
            if "feature_key" in dictionary.keys()\
                else APIHelper.SKIP
        grants = None
        if dictionary.get("grants") is not None:
            grants = [
                WalletGrant.from_dictionary(x)
                    for x in dictionary.get("grants")
            ]
        else:
            grants = APIHelper.SKIP
        recurring_funding = None
        if dictionary.get("recurring_funding") is not None:
            recurring_funding = [
                WalletRecurringFunding.from_dictionary(x)
                    for x in dictionary.get("recurring_funding")
            ]
        else:
            recurring_funding = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_at")).datetime\
            if dictionary.get("updated_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   owner_type,
                   owner_id,
                   name,
                   wallet_product_id,
                   wallet_product_name,
                   unit,
                   price_point_id,
                   balance,
                   posted_balance,
                   meter,
                   metered_through_at,
                   metered_recheck_after_seconds,
                   metered_stale,
                   status,
                   depletion_policy,
                   hard_stop_overflow,
                   origin,
                   feature_key,
                   grants,
                   recurring_funding,
                   created_at,
                   updated_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _owner_type=(
            self.owner_type
            if hasattr(self, "owner_type")
            else None
        )
        _owner_id=(
            self.owner_id
            if hasattr(self, "owner_id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _wallet_product_id=(
            self.wallet_product_id
            if hasattr(self, "wallet_product_id")
            else None
        )
        _wallet_product_name=(
            self.wallet_product_name
            if hasattr(self, "wallet_product_name")
            else None
        )
        _unit=(
            self.unit
            if hasattr(self, "unit")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _balance=(
            self.balance
            if hasattr(self, "balance")
            else None
        )
        _posted_balance=(
            self.posted_balance
            if hasattr(self, "posted_balance")
            else None
        )
        _meter=(
            self.meter
            if hasattr(self, "meter")
            else None
        )
        _metered_through_at=(
            self.metered_through_at
            if hasattr(self, "metered_through_at")
            else None
        )
        _metered_recheck_after_seconds=(
            self.metered_recheck_after_seconds
            if hasattr(self, "metered_recheck_after_seconds")
            else None
        )
        _metered_stale=(
            self.metered_stale
            if hasattr(self, "metered_stale")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _depletion_policy=(
            self.depletion_policy
            if hasattr(self, "depletion_policy")
            else None
        )
        _hard_stop_overflow=(
            self.hard_stop_overflow
            if hasattr(self, "hard_stop_overflow")
            else None
        )
        _origin=(
            self.origin
            if hasattr(self, "origin")
            else None
        )
        _feature_key=(
            self.feature_key
            if hasattr(self, "feature_key")
            else None
        )
        _grants=(
            self.grants
            if hasattr(self, "grants")
            else None
        )
        _recurring_funding=(
            self.recurring_funding
            if hasattr(self, "recurring_funding")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"owner_type={_owner_type!r}, "
            f"owner_id={_owner_id!r}, "
            f"name={_name!r}, "
            f"wallet_product_id={_wallet_product_id!r}, "
            f"wallet_product_name={_wallet_product_name!r}, "
            f"unit={_unit!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"balance={_balance!r}, "
            f"posted_balance={_posted_balance!r}, "
            f"meter={_meter!r}, "
            f"metered_through_at={_metered_through_at!r}, "
            f"metered_recheck_after_seconds={_metered_recheck_after_seconds!r}, "
            f"metered_stale={_metered_stale!r}, "
            f"status={_status!r}, "
            f"depletion_policy={_depletion_policy!r}, "
            f"hard_stop_overflow={_hard_stop_overflow!r}, "
            f"origin={_origin!r}, "
            f"feature_key={_feature_key!r}, "
            f"grants={_grants!r}, "
            f"recurring_funding={_recurring_funding!r}, "
            f"created_at={_created_at!r}, "
            f"updated_at={_updated_at!r}, "
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
        _owner_type=(
            self.owner_type
            if hasattr(self, "owner_type")
            else None
        )
        _owner_id=(
            self.owner_id
            if hasattr(self, "owner_id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _wallet_product_id=(
            self.wallet_product_id
            if hasattr(self, "wallet_product_id")
            else None
        )
        _wallet_product_name=(
            self.wallet_product_name
            if hasattr(self, "wallet_product_name")
            else None
        )
        _unit=(
            self.unit
            if hasattr(self, "unit")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _balance=(
            self.balance
            if hasattr(self, "balance")
            else None
        )
        _posted_balance=(
            self.posted_balance
            if hasattr(self, "posted_balance")
            else None
        )
        _meter=(
            self.meter
            if hasattr(self, "meter")
            else None
        )
        _metered_through_at=(
            self.metered_through_at
            if hasattr(self, "metered_through_at")
            else None
        )
        _metered_recheck_after_seconds=(
            self.metered_recheck_after_seconds
            if hasattr(self, "metered_recheck_after_seconds")
            else None
        )
        _metered_stale=(
            self.metered_stale
            if hasattr(self, "metered_stale")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _depletion_policy=(
            self.depletion_policy
            if hasattr(self, "depletion_policy")
            else None
        )
        _hard_stop_overflow=(
            self.hard_stop_overflow
            if hasattr(self, "hard_stop_overflow")
            else None
        )
        _origin=(
            self.origin
            if hasattr(self, "origin")
            else None
        )
        _feature_key=(
            self.feature_key
            if hasattr(self, "feature_key")
            else None
        )
        _grants=(
            self.grants
            if hasattr(self, "grants")
            else None
        )
        _recurring_funding=(
            self.recurring_funding
            if hasattr(self, "recurring_funding")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"owner_type={_owner_type!s}, "
            f"owner_id={_owner_id!s}, "
            f"name={_name!s}, "
            f"wallet_product_id={_wallet_product_id!s}, "
            f"wallet_product_name={_wallet_product_name!s}, "
            f"unit={_unit!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"balance={_balance!s}, "
            f"posted_balance={_posted_balance!s}, "
            f"meter={_meter!s}, "
            f"metered_through_at={_metered_through_at!s}, "
            f"metered_recheck_after_seconds={_metered_recheck_after_seconds!s}, "
            f"metered_stale={_metered_stale!s}, "
            f"status={_status!s}, "
            f"depletion_policy={_depletion_policy!s}, "
            f"hard_stop_overflow={_hard_stop_overflow!s}, "
            f"origin={_origin!s}, "
            f"feature_key={_feature_key!s}, "
            f"grants={_grants!s}, "
            f"recurring_funding={_recurring_funding!s}, "
            f"created_at={_created_at!s}, "
            f"updated_at={_updated_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
