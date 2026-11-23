"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class WalletProductUsageCount(object):
    """Implementation of the 'Wallet Product Usage Count' model.

    A rollup of what's using this Wallet Product, for the catalog listing.

    Attributes:
        wallet_configurations (int): Number of wallet templates billing through this
            product, whether or not any wallet has been created from them yet.
        active_wallets (int): Number of active (non-archived) wallets currently
            denominated by this product.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallet_configurations": "wallet_configurations",
        "active_wallets": "active_wallets",
    }

    def __init__(
        self,
        wallet_configurations=None,
        active_wallets=None,
        additional_properties=None):
        """Initialize a WalletProductUsageCount instance."""
        # Initialize members of the class
        self.wallet_configurations = wallet_configurations
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
        wallet_configurations =\
            dictionary.get("wallet_configurations")\
            if dictionary.get("wallet_configurations")\
                else None
        active_wallets =\
            dictionary.get("active_wallets")\
            if dictionary.get("active_wallets")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallet_configurations,
                   active_wallets,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallet_configurations=self.wallet_configurations
        _active_wallets=self.active_wallets
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_configurations={_wallet_configurations!r}, "
            f"active_wallets={_active_wallets!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallet_configurations=self.wallet_configurations
        _active_wallets=self.active_wallets
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallet_configurations={_wallet_configurations!s}, "
            f"active_wallets={_active_wallets!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
