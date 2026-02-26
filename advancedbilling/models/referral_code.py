"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ReferralCode(object):
    """Implementation of the 'Referral Code' model.

    Attributes:
        id (int): The model property of type int.
        site_id (int): The model property of type int.
        subscription_id (int): The model property of type int.
        code (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "site_id": "site_id",
        "subscription_id": "subscription_id",
        "code": "code",
    }

    _optionals = [
        "id",
        "site_id",
        "subscription_id",
        "code",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        site_id=APIHelper.SKIP,
        subscription_id=APIHelper.SKIP,
        code=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ReferralCode instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id
        if code is not APIHelper.SKIP:
            self.code = code

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        site_id =\
            dictionary.get("site_id")\
            if dictionary.get("site_id")\
                else APIHelper.SKIP
        subscription_id =\
            dictionary.get("subscription_id")\
            if dictionary.get("subscription_id")\
                else APIHelper.SKIP
        code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   site_id,
                   subscription_id,
                   code,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"site_id={_site_id!r}, "
            f"subscription_id={_subscription_id!r}, "
            f"code={_code!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"site_id={_site_id!s}, "
            f"subscription_id={_subscription_id!s}, "
            f"code={_code!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
