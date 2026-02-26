"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ProformaInvoiceCredit(object):
    """Implementation of the 'Proforma Invoice Credit' model.

    Attributes:
        uid (str): The model property of type str.
        memo (str): The model property of type str.
        original_amount (str): The model property of type str.
        applied_amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": "uid",
        "memo": "memo",
        "original_amount": "original_amount",
        "applied_amount": "applied_amount",
    }

    _optionals = [
        "uid",
        "memo",
        "original_amount",
        "applied_amount",
    ]

    def __init__(
        self,
        uid=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        original_amount=APIHelper.SKIP,
        applied_amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ProformaInvoiceCredit instance."""
        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount

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
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP
        original_amount =\
            dictionary.get("original_amount")\
            if dictionary.get("original_amount")\
                else APIHelper.SKIP
        applied_amount =\
            dictionary.get("applied_amount")\
            if dictionary.get("applied_amount")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(uid,
                   memo,
                   original_amount,
                   applied_amount,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _original_amount=(
            self.original_amount
            if hasattr(self, "original_amount")
            else None
        )
        _applied_amount=(
            self.applied_amount
            if hasattr(self, "applied_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"memo={_memo!r}, "
            f"original_amount={_original_amount!r}, "
            f"applied_amount={_applied_amount!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _original_amount=(
            self.original_amount
            if hasattr(self, "original_amount")
            else None
        )
        _applied_amount=(
            self.applied_amount
            if hasattr(self, "applied_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"memo={_memo!s}, "
            f"original_amount={_original_amount!s}, "
            f"applied_amount={_applied_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
