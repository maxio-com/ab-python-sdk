"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Purchase(object):
    """Implementation of the 'Purchase' model.

    Attributes:
        quantity (str | int): The number of wallet units to purchase, as a decimal
            string with at most 8 fractional digits. Send fractional values as
            strings: a JSON number with a decimal point is rejected with `422`,
            because a double-precision float may already have lost precision before
            the request arrives.
        price_point_id (int): The price point to purchase at. Must belong to the
            wallet's billing product. Defaults to the `price_point_id` set on the
            wallet.
        memo (str): (Optional) A note recorded on the resulting grant's ledger row.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": "quantity",
        "price_point_id": "price_point_id",
        "memo": "memo",
    }

    _optionals = [
        "price_point_id",
        "memo",
    ]

    _nullables = [
        "memo",
    ]

    def __init__(
        self,
        quantity=None,
        price_point_id=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Purchase instance."""
        # Initialize members of the class
        self.quantity = quantity
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if memo is not APIHelper.SKIP:
            self.memo = memo

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
        quantity = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("PurchaseQuantity"),
            dictionary.get("quantity"),
            False)\
            if dictionary.get("quantity") is not None\
            else None
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if "memo" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(quantity,
                   price_point_id,
                   memo,
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
            return (UnionTypeLookUp.get("PurchaseQuantity")
                .validate(dictionary.quantity).is_valid)

        if not isinstance(dictionary, dict):
            return False

        return (UnionTypeLookUp.get("PurchaseQuantity")
            .validate(dictionary.get("quantity")).is_valid)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _quantity=self.quantity
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"quantity={_quantity!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"memo={_memo!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _quantity=self.quantity
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"quantity={_quantity!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"memo={_memo!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
