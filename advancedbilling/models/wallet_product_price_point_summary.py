"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class WalletProductPricePointSummary(object):
    """Implementation of the 'Wallet Product Price Point Summary' model.

    A summary of the Wallet Product's default price point, for rendering a catalog
    listing without a separate price points call.

    Attributes:
        archived_count (int): Number of archived price points on this Wallet Product.
        pricing_scheme (str): The default price point's pricing scheme. `null` if the
            Wallet Product has no default price point.
        tier_count (int): Number of price brackets on the default price point. A
            `per_unit` scheme always stores exactly one synthesized bracket, so this
            is `1` for `per_unit`, not `0`.
        entry_price (str): The unit price of the default price point's first bracket,
            as a decimal string. `null` if there are no brackets.
        final_price (str): The unit price of the default price point's last bracket,
            as a decimal string. `null` if there are no brackets.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archived_count": "archived_count",
        "pricing_scheme": "pricing_scheme",
        "tier_count": "tier_count",
        "entry_price": "entry_price",
        "final_price": "final_price",
    }

    _optionals = [
        "archived_count",
        "pricing_scheme",
        "tier_count",
        "entry_price",
        "final_price",
    ]

    _nullables = [
        "pricing_scheme",
        "entry_price",
        "final_price",
    ]

    def __init__(
        self,
        archived_count=APIHelper.SKIP,
        pricing_scheme=APIHelper.SKIP,
        tier_count=APIHelper.SKIP,
        entry_price=APIHelper.SKIP,
        final_price=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletProductPricePointSummary instance."""
        # Initialize members of the class
        if archived_count is not APIHelper.SKIP:
            self.archived_count = archived_count
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme
        if tier_count is not APIHelper.SKIP:
            self.tier_count = tier_count
        if entry_price is not APIHelper.SKIP:
            self.entry_price = entry_price
        if final_price is not APIHelper.SKIP:
            self.final_price = final_price

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
        archived_count =\
            dictionary.get("archived_count")\
            if dictionary.get("archived_count")\
                else APIHelper.SKIP
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if "pricing_scheme" in dictionary.keys()\
                else APIHelper.SKIP
        tier_count =\
            dictionary.get("tier_count")\
            if dictionary.get("tier_count")\
                else APIHelper.SKIP
        entry_price =\
            dictionary.get("entry_price")\
            if "entry_price" in dictionary.keys()\
                else APIHelper.SKIP
        final_price =\
            dictionary.get("final_price")\
            if "final_price" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(archived_count,
                   pricing_scheme,
                   tier_count,
                   entry_price,
                   final_price,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _archived_count=(
            self.archived_count
            if hasattr(self, "archived_count")
            else None
        )
        _pricing_scheme=(
            self.pricing_scheme
            if hasattr(self, "pricing_scheme")
            else None
        )
        _tier_count=(
            self.tier_count
            if hasattr(self, "tier_count")
            else None
        )
        _entry_price=(
            self.entry_price
            if hasattr(self, "entry_price")
            else None
        )
        _final_price=(
            self.final_price
            if hasattr(self, "final_price")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"archived_count={_archived_count!r}, "
            f"pricing_scheme={_pricing_scheme!r}, "
            f"tier_count={_tier_count!r}, "
            f"entry_price={_entry_price!r}, "
            f"final_price={_final_price!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _archived_count=(
            self.archived_count
            if hasattr(self, "archived_count")
            else None
        )
        _pricing_scheme=(
            self.pricing_scheme
            if hasattr(self, "pricing_scheme")
            else None
        )
        _tier_count=(
            self.tier_count
            if hasattr(self, "tier_count")
            else None
        )
        _entry_price=(
            self.entry_price
            if hasattr(self, "entry_price")
            else None
        )
        _final_price=(
            self.final_price
            if hasattr(self, "final_price")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"archived_count={_archived_count!s}, "
            f"pricing_scheme={_pricing_scheme!s}, "
            f"tier_count={_tier_count!s}, "
            f"entry_price={_entry_price!s}, "
            f"final_price={_final_price!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
