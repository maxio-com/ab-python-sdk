"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class Origin(object):
    """Implementation of the 'Origin' enum.

    How the grant was created. `recurring` comes from the wallet's automatic funding
    schedule (see the wallet's `recurring_funding` array). `manual` comes from a
    one-time grant posted to [Create Wallet
    Transaction]($e/Wallet%20Transactions/createWalletTransaction). `initial_balance`
    comes from a non-zero `initial_balance` at wallet creation. `allowance_increase`
    comes from raising a funding entitlement's allowance while it's already funding a
    wallet. `purchase` comes from [Create Wallet
    Purchase]($e/Wallet%20Purchases/createWalletPurchase).

    Attributes:
        RECURRING: The enum member of type str.
        MANUAL: The enum member of type str.
        INITIAL_BALANCE: The enum member of type str.
        ALLOWANCE_INCREASE: The enum member of type str.
        PURCHASE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    RECURRING = "recurring"

    MANUAL = "manual"

    INITIAL_BALANCE = "initial_balance"

    ALLOWANCE_INCREASE = "allowance_increase"

    PURCHASE = "purchase"

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
