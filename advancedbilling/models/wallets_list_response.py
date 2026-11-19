"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.list_public_keys_meta import (
    ListPublicKeysMeta,
)
from advancedbilling.models.wallet import Wallet


class WalletsListResponse(object):
    """Implementation of the 'Wallets List Response' model.

    Attributes:
        wallets (List[Wallet]): The model property of type List[Wallet].
        meta (ListPublicKeysMeta): The model property of type ListPublicKeysMeta.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wallets": "wallets",
        "meta": "meta",
    }

    def __init__(
        self,
        wallets=None,
        meta=None,
        additional_properties=None):
        """Initialize a WalletsListResponse instance."""
        # Initialize members of the class
        self.wallets = wallets
        self.meta = meta

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
        wallets = None
        if dictionary.get("wallets") is not None:
            wallets = [
                Wallet.from_dictionary(x)
                    for x in dictionary.get("wallets")
            ]
        meta =\
            ListPublicKeysMeta.from_dictionary(
                dictionary.get("meta"))\
                if dictionary.get("meta") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(wallets,
                   meta,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wallets=self.wallets
        _meta=self.meta
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallets={_wallets!r}, "
            f"meta={_meta!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wallets=self.wallets
        _meta=self.meta
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wallets={_wallets!s}, "
            f"meta={_meta!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
