"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.active_wallets import (
    ActiveWallets,
)
from advancedbilling.models.wallet_product_usage_template import (
    WalletProductUsageTemplate,
)


class WalletProductUsageResponse(object):
    """Implementation of the 'Wallet Product Usage Response' model.

    Attributes:
        wallet_templates (List[WalletProductUsageTemplate]): Wallet templates billing
            through this product at its default price point.
        price_point_overrides (List[WalletProductUsageTemplate]): Wallet templates
            billing through this product at a price point other than the default.
        active_wallets (ActiveWallets): The model property of type ActiveWallets.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_templates": "wallet_templates",
        "price_point_overrides": "price_point_overrides",
        "active_wallets": "active_wallets",
    }

    def __init__(
        self,
        wallet_templates=None,
        price_point_overrides=None,
        active_wallets=None,
        additional_properties=None):
        """Initialize a WalletProductUsageResponse instance."""
        # Initialize members of the class
        self.wallet_templates = wallet_templates
        self.price_point_overrides = price_point_overrides
        self.active_wallets = active_wallets

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
        wallet_templates = None
        if dictionary.get("wallet_templates") is not None:
            wallet_templates = [
                WalletProductUsageTemplate.from_dictionary(x)
                    for x in dictionary.get("wallet_templates")
            ]
        price_point_overrides = None
        if dictionary.get("price_point_overrides") is not None:
            price_point_overrides = [
                WalletProductUsageTemplate.from_dictionary(x)
                    for x in dictionary.get("price_point_overrides")
            ]
        active_wallets =\
            ActiveWallets.from_dictionary(
                dictionary.get("active_wallets"))\
                if dictionary.get("active_wallets") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_templates,
                   price_point_overrides,
                   active_wallets,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_templates=self.wallet_templates
        _price_point_overrides=self.price_point_overrides
        _active_wallets=self.active_wallets
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_templates={_wallet_templates!r}, "
            f"price_point_overrides={_price_point_overrides!r}, "
            f"active_wallets={_active_wallets!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_templates=self.wallet_templates
        _price_point_overrides=self.price_point_overrides
        _active_wallets=self.active_wallets
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_templates={_wallet_templates!s}, "
            f"price_point_overrides={_price_point_overrides!s}, "
            f"active_wallets={_active_wallets!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
