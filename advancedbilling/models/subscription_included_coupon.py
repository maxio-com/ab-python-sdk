"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class SubscriptionIncludedCoupon(object):
    """Implementation of the 'Subscription Included Coupon' model.

    Attributes:
        code (str): The model property of type str.
        use_count (int): The model property of type int.
        uses_allowed (int): The model property of type int.
        expires_at (str): The model property of type str.
        recurring (bool): The model property of type bool.
        amount_in_cents (int): The model property of type int.
        percentage (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": "code",
        "use_count": "use_count",
        "uses_allowed": "uses_allowed",
        "expires_at": "expires_at",
        "recurring": "recurring",
        "amount_in_cents": "amount_in_cents",
        "percentage": "percentage",
    }

    _optionals = [
        "code",
        "use_count",
        "uses_allowed",
        "expires_at",
        "recurring",
        "amount_in_cents",
        "percentage",
    ]

    _nullables = [
        "expires_at",
        "amount_in_cents",
        "percentage",
    ]

    def __init__(
        self,
        code=APIHelper.SKIP,
        use_count=APIHelper.SKIP,
        uses_allowed=APIHelper.SKIP,
        expires_at=APIHelper.SKIP,
        recurring=APIHelper.SKIP,
        amount_in_cents=APIHelper.SKIP,
        percentage=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionIncludedCoupon instance."""
        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code
        if use_count is not APIHelper.SKIP:
            self.use_count = use_count
        if uses_allowed is not APIHelper.SKIP:
            self.uses_allowed = uses_allowed
        if expires_at is not APIHelper.SKIP:
            self.expires_at = expires_at
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage

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
        code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else APIHelper.SKIP
        use_count =\
            dictionary.get("use_count")\
            if dictionary.get("use_count")\
                else APIHelper.SKIP
        uses_allowed =\
            dictionary.get("uses_allowed")\
            if dictionary.get("uses_allowed")\
                else APIHelper.SKIP
        expires_at =\
            dictionary.get("expires_at")\
            if "expires_at" in dictionary.keys()\
                else APIHelper.SKIP
        recurring =\
            dictionary.get("recurring")\
            if "recurring" in dictionary.keys()\
                else APIHelper.SKIP
        amount_in_cents =\
            dictionary.get("amount_in_cents")\
            if "amount_in_cents" in dictionary.keys()\
                else APIHelper.SKIP
        percentage =\
            dictionary.get("percentage")\
            if "percentage" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(code,
                   use_count,
                   uses_allowed,
                   expires_at,
                   recurring,
                   amount_in_cents,
                   percentage,
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
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _use_count=(
            self.use_count
            if hasattr(self, "use_count")
            else None
        )
        _uses_allowed=(
            self.uses_allowed
            if hasattr(self, "uses_allowed")
            else None
        )
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _recurring=(
            self.recurring
            if hasattr(self, "recurring")
            else None
        )
        _amount_in_cents=(
            self.amount_in_cents
            if hasattr(self, "amount_in_cents")
            else None
        )
        _percentage=(
            self.percentage
            if hasattr(self, "percentage")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!r}, "
            f"use_count={_use_count!r}, "
            f"uses_allowed={_uses_allowed!r}, "
            f"expires_at={_expires_at!r}, "
            f"recurring={_recurring!r}, "
            f"amount_in_cents={_amount_in_cents!r}, "
            f"percentage={_percentage!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _use_count=(
            self.use_count
            if hasattr(self, "use_count")
            else None
        )
        _uses_allowed=(
            self.uses_allowed
            if hasattr(self, "uses_allowed")
            else None
        )
        _expires_at=(
            self.expires_at
            if hasattr(self, "expires_at")
            else None
        )
        _recurring=(
            self.recurring
            if hasattr(self, "recurring")
            else None
        )
        _amount_in_cents=(
            self.amount_in_cents
            if hasattr(self, "amount_in_cents")
            else None
        )
        _percentage=(
            self.percentage
            if hasattr(self, "percentage")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!s}, "
            f"use_count={_use_count!s}, "
            f"uses_allowed={_uses_allowed!s}, "
            f"expires_at={_expires_at!s}, "
            f"recurring={_recurring!s}, "
            f"amount_in_cents={_amount_in_cents!s}, "
            f"percentage={_percentage!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
