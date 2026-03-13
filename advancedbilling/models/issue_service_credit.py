"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class IssueServiceCredit(object):
    """Implementation of the 'Issue Service Credit' model.

    Attributes:
        amount (float | str): The model property of type float | str.
        memo (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "memo": "memo",
    }

    _optionals = [
        "memo",
    ]

    def __init__(
        self,
        amount=None,
        memo=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a IssueServiceCredit instance."""
        # Initialize members of the class
        self.amount = amount
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
        amount = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("IssueServiceCreditAmount"),
            dictionary.get("amount"),
            False)\
            if dictionary.get("amount") is not None\
            else None
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(amount,
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
            return (UnionTypeLookUp.get("IssueServiceCreditAmount")
                .validate(dictionary.amount).is_valid)

        if not isinstance(dictionary, dict):
            return False

        return (UnionTypeLookUp.get("IssueServiceCreditAmount")
            .validate(dictionary.get("amount")).is_valid)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _amount=self.amount
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!r}, "
            f"memo={_memo!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _amount=self.amount
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!s}, "
            f"memo={_memo!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
