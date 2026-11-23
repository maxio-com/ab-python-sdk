"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class WalletOrigin(object):
    """Implementation of the 'Wallet Origin' enum.

    How the wallet came to exist. `manual` for a wallet created directly with [Create
    Wallet]($e/Wallets/createWallet). `feature` for a wallet auto-provisioned because
    a subscription resolved a usage-limit entitlement whose Feature has
    `wallet_behavior` configured.

    Attributes:
        MANUAL: The enum member of type str.
        FEATURE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    MANUAL = "manual"

    FEATURE = "feature"

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
