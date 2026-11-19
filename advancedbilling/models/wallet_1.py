"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Wallet1(object):
    """Implementation of the 'Wallet1' model.

    Attributes:
        subscription_id (int): The subscription that will own the wallet.
        wallet_product_id (int | str): The [Wallet
            Product]($e/Wallet%20Products/createWalletProduct) that will denominate
            the wallet: its numeric id, or its handle prefixed with `handle:` (for
            example `handle:token-pack`). A bare handle with no prefix is looked up
            as an id and returns `404`. Immutable once the wallet is created.
        name (str): (Optional) A merchant-facing label for the wallet. Surrounding
            spaces are stripped; a blank value is stored as `null`.
        depletion_policy (str): Defaults to `hard_stop`, currently the only supported
            value.
        hard_stop_overflow (WalletHardStopOverflow): Defaults to `discard`.
        meter_id (int): Pairs the wallet with a merchant-owned metering meter, so its
            balance factors in live usage (see the wallet resource's `meter` and
            `metered_through_at` fields). Only a `sum` or `count` meter can be
            paired. Requires metered wallet consumption to be enabled for the site,
            checked whenever this or `conversion_rate` is sent: `403` (plain text,
            not JSON) if it isn't. A meter id that doesn't resolve to a
            merchant-owned meter on this site, including a system-maintained shadow
            meter, is `404`. Immutable once the wallet is created.
        conversion_rate (str | int | None): How many wallet units one meter unit is
            worth, as a decimal string with at most 8 fractional digits, greater than
            `0` and below 10^16. Send fractional values as strings: a JSON number
            with a decimal point is rejected with `422`, because a double-precision
            float may already have lost precision before the request arrives. Only
            meaningful with `meter_id`. Defaults to `"1.0"`. Immutable once the
            wallet is created.
        price_point_id (int): The price point used to price [Create Wallet
            Purchase]($e/Wallet%20Purchases/createWalletPurchase) calls against this
            wallet. Must belong to the Wallet Product, and can't be archived or a
            subscription-specific custom price point. Defaults to the Wallet
            Product's default price point. Immutable once the wallet is created.
        initial_balance (str | int | None): (Optional) A free opening balance, not a
            purchase and not reflected on any invoice. When non-zero, wallet creation
            also writes an initial-balance grant and a matching `initial_balance`
            ledger row. Omitted or exactly `0` creates a zero-balance wallet, not an
            error. Encoded as a decimal string with at most 8 fractional digits, and
            must be non-negative and below 10^16. Send fractional values as strings:
            a JSON number with a decimal point is rejected with `422`, because a
            double-precision float may already have lost precision before the request
            arrives.
        initial_balance_expires_at (str): An expiration for the initial-balance
            grant. Only accepted together with a non-zero `initial_balance`, and must
            be in the future. Accepts either a bare calendar date (`YYYY-MM-DD`),
            resolved to the end of that day in the site's time zone, or a full
            timestamp. A calendar day that doesn't exist, such as `2027-02-30`, is
            rejected with `422` rather than rolled into the next month.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": "subscription_id",
        "wallet_product_id": "wallet_product_id",
        "name": "name",
        "depletion_policy": "depletion_policy",
        "hard_stop_overflow": "hard_stop_overflow",
        "meter_id": "meter_id",
        "conversion_rate": "conversion_rate",
        "price_point_id": "price_point_id",
        "initial_balance": "initial_balance",
        "initial_balance_expires_at": "initial_balance_expires_at",
    }

    _optionals = [
        "name",
        "depletion_policy",
        "hard_stop_overflow",
        "meter_id",
        "conversion_rate",
        "price_point_id",
        "initial_balance",
        "initial_balance_expires_at",
    ]

    _nullables = [
        "name",
        "initial_balance_expires_at",
    ]

    def __init__(
        self,
        subscription_id=None,
        wallet_product_id=None,
        name=APIHelper.SKIP,
        depletion_policy=APIHelper.SKIP,
        hard_stop_overflow=APIHelper.SKIP,
        meter_id=APIHelper.SKIP,
        conversion_rate=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        initial_balance=APIHelper.SKIP,
        initial_balance_expires_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Wallet1 instance."""
        # Initialize members of the class
        self.subscription_id = subscription_id
        self.wallet_product_id = wallet_product_id
        if name is not APIHelper.SKIP:
            self.name = name
        if depletion_policy is not APIHelper.SKIP:
            self.depletion_policy = depletion_policy
        if hard_stop_overflow is not APIHelper.SKIP:
            self.hard_stop_overflow = hard_stop_overflow
        if meter_id is not APIHelper.SKIP:
            self.meter_id = meter_id
        if conversion_rate is not APIHelper.SKIP:
            self.conversion_rate = conversion_rate
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if initial_balance is not APIHelper.SKIP:
            self.initial_balance = initial_balance
        if initial_balance_expires_at is not APIHelper.SKIP:
            self.initial_balance_expires_at = initial_balance_expires_at

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
        subscription_id =\
            dictionary.get("subscription_id")\
            if dictionary.get("subscription_id")\
                else None
        wallet_product_id = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("Wallet1WalletProductId"),
            dictionary.get("wallet_product_id"),
            False)\
            if dictionary.get("wallet_product_id") is not None\
            else None
        name =\
            dictionary.get("name")\
            if "name" in dictionary.keys()\
                else APIHelper.SKIP
        depletion_policy =\
            dictionary.get("depletion_policy")\
            if dictionary.get("depletion_policy")\
                else APIHelper.SKIP
        hard_stop_overflow =\
            dictionary.get("hard_stop_overflow")\
            if dictionary.get("hard_stop_overflow")\
                else APIHelper.SKIP
        meter_id =\
            dictionary.get("meter_id")\
            if dictionary.get("meter_id")\
                else APIHelper.SKIP
        conversion_rate = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("Wallet1ConversionRate"),
            dictionary.get("conversion_rate"),
            False)\
            if dictionary.get("conversion_rate") is not None\
            else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP
        initial_balance = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("Wallet1InitialBalance"),
            dictionary.get("initial_balance"),
            False)\
            if dictionary.get("initial_balance") is not None\
            else APIHelper.SKIP
        initial_balance_expires_at =\
            dictionary.get("initial_balance_expires_at")\
            if "initial_balance_expires_at" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(subscription_id,
                   wallet_product_id,
                   name,
                   depletion_policy,
                   hard_stop_overflow,
                   meter_id,
                   conversion_rate,
                   price_point_id,
                   initial_balance,
                   initial_balance_expires_at,
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
            return APIHelper.is_valid_type(
                    value=dictionary.subscription_id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        int,
                )) \
                and (UnionTypeLookUp.get("Wallet1WalletProductId")
                .validate(dictionary.wallet_product_id).is_valid)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("subscription_id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    int,
            )) \
            and (UnionTypeLookUp.get("Wallet1WalletProductId")
            .validate(dictionary.get("wallet_product_id")).is_valid)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _subscription_id=self.subscription_id
        _wallet_product_id=self.wallet_product_id
        _name=(
            self.name
            if hasattr(self, "name")
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
        _meter_id=(
            self.meter_id
            if hasattr(self, "meter_id")
            else None
        )
        _conversion_rate=(
            self.conversion_rate
            if hasattr(self, "conversion_rate")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _initial_balance=(
            self.initial_balance
            if hasattr(self, "initial_balance")
            else None
        )
        _initial_balance_expires_at=(
            self.initial_balance_expires_at
            if hasattr(self, "initial_balance_expires_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription_id={_subscription_id!r}, "
            f"wallet_product_id={_wallet_product_id!r}, "
            f"name={_name!r}, "
            f"depletion_policy={_depletion_policy!r}, "
            f"hard_stop_overflow={_hard_stop_overflow!r}, "
            f"meter_id={_meter_id!r}, "
            f"conversion_rate={_conversion_rate!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"initial_balance={_initial_balance!r}, "
            f"initial_balance_expires_at={_initial_balance_expires_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _subscription_id=self.subscription_id
        _wallet_product_id=self.wallet_product_id
        _name=(
            self.name
            if hasattr(self, "name")
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
        _meter_id=(
            self.meter_id
            if hasattr(self, "meter_id")
            else None
        )
        _conversion_rate=(
            self.conversion_rate
            if hasattr(self, "conversion_rate")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _initial_balance=(
            self.initial_balance
            if hasattr(self, "initial_balance")
            else None
        )
        _initial_balance_expires_at=(
            self.initial_balance_expires_at
            if hasattr(self, "initial_balance_expires_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription_id={_subscription_id!s}, "
            f"wallet_product_id={_wallet_product_id!s}, "
            f"name={_name!s}, "
            f"depletion_policy={_depletion_policy!s}, "
            f"hard_stop_overflow={_hard_stop_overflow!s}, "
            f"meter_id={_meter_id!s}, "
            f"conversion_rate={_conversion_rate!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"initial_balance={_initial_balance!s}, "
            f"initial_balance_expires_at={_initial_balance_expires_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
