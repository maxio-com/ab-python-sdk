"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.wallet_product_active_wallet import (
    WalletProductActiveWallet,
)


class ActiveWallets(object):
    """Implementation of the 'ActiveWallets' model.

    Attributes:
        total (int): Total count of active wallets drawing on this product.
        sample (List[WalletProductActiveWallet]): Up to 50 of the most recently
            created active wallets, newest first.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total": "total",
        "sample": "sample",
    }

    def __init__(
        self,
        total=None,
        sample=None,
        additional_properties=None):
        """Initialize a ActiveWallets instance."""
        # Initialize members of the class
        self.total = total
        self.sample = sample

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
        total =\
            dictionary.get("total")\
            if dictionary.get("total")\
                else None
        sample = None
        if dictionary.get("sample") is not None:
            sample = [
                WalletProductActiveWallet.from_dictionary(x)
                    for x in dictionary.get("sample")
            ]

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(total,
                   sample,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _total=self.total
        _sample=self.sample
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"total={_total!r}, "
            f"sample={_sample!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _total=self.total
        _sample=self.sample
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"total={_total!s}, "
            f"sample={_sample!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
