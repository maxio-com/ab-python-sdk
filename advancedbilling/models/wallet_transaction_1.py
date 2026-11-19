"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.kind_1 import Kind1


class WalletTransaction1(object):
    """Implementation of the 'WalletTransaction1' model.

    Attributes:
        kind (Kind1): Determines the direction of the movement. The amount itself is
            always sent positive.
        amount (str | int): Always positive; `kind` determines the sign written to
            the ledger. Encoded as a decimal string with at most 8 fractional digits.
            Send fractional values as strings: a JSON number with a decimal point is
            rejected with `422`, because a double-precision float may already have
            lost precision before the request arrives.
        memo (str): The model property of type str.
        expires_at (str): An expiration for the grant this creates. Only accepted
            with `kind: grant`; sending it with `kind: debit` is rejected. Omit it
            for an evergreen grant. Accepts either a bare calendar date
            (`YYYY-MM-DD`), resolved to the end of that day in the site's time zone,
            or a full timestamp. A calendar day that doesn't exist, such as
            `2027-02-30`, is rejected with `422` rather than rolled into the next
            month.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kind": "kind",
        "amount": "amount",
        "memo": "memo",
        "expires_at": "expires_at",
    }

    _optionals = [
        "memo",
        "expires_at",
    ]

    _nullables = [
        "memo",
        "expires_at",
    ]

    def __init__(
        self,
        kind=None,
        amount=None,
        memo=APIHelper.SKIP,
        expires_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletTransaction1 instance."""
        # Initialize members of the class
        self.kind = kind
        self.amount = amount
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if expires_at is not APIHelper.SKIP:
            self.expires_at = expires_at

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
        kind =\
            dictionary.get("kind")\
            if dictionary.get("kind")\
                else None
        amount = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("WalletTransaction1Amount"),
            dictionary.get("amount"),
            False)\
            if dictionary.get("amount") is not None\
            else None
        memo =\
            dictionary.get("memo")\
            if "memo" in dictionary.keys()\
                else APIHelper.SKIP
        expires_at =\
            dictionary.get("expires_at")\
            if "expires_at" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(kind,
                   amount,
                   memo,
                   expires_at,
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
                    value=dictionary.kind,
                    type_callable=lambda value:
                        Kind1.validate(value)) \
                and (UnionTypeLookUp.get("WalletTransaction1Amount")
                .validate(dictionary.amount).is_valid)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("kind"),
                type_callable=lambda value:
                    Kind1.validate(value)) \
            and (UnionTypeLookUp.get("WalletTransaction1Amount")
            .validate(dictionary.get("amount")).is_valid)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _kind=self.kind
        _amount=self.amount
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"kind={_kind!r}, "
            f"amount={_amount!r}, "
            f"memo={_memo!r}, "
            f"expires_at={_expires_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _kind=self.kind
        _amount=self.amount
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"kind={_kind!s}, "
            f"amount={_amount!s}, "
            f"memo={_memo!s}, "
            f"expires_at={_expires_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
