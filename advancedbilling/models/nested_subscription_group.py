"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class NestedSubscriptionGroup(object):
    """Implementation of the 'Nested Subscription Group' model.

    Attributes:
        uid (str): The UID for the group
        scheme (int): Whether the group is configured to rely on a primary
            subscription for billing. At this time, it will always be 1.
        primary_subscription_id (int): The subscription ID of the primary within the
            group. Applicable to scheme 1.
        primary (bool): A boolean indicating whether the subscription is the primary
            in the group. Applicable to scheme 1.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": "uid",
        "scheme": "scheme",
        "primary_subscription_id": "primary_subscription_id",
        "primary": "primary",
    }

    _optionals = [
        "uid",
        "scheme",
        "primary_subscription_id",
        "primary",
    ]

    def __init__(
        self,
        uid=APIHelper.SKIP,
        scheme=APIHelper.SKIP,
        primary_subscription_id=APIHelper.SKIP,
        primary=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a NestedSubscriptionGroup instance."""
        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid
        if scheme is not APIHelper.SKIP:
            self.scheme = scheme
        if primary_subscription_id is not APIHelper.SKIP:
            self.primary_subscription_id = primary_subscription_id
        if primary is not APIHelper.SKIP:
            self.primary = primary

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
        scheme =\
            dictionary.get("scheme")\
            if dictionary.get("scheme")\
                else APIHelper.SKIP
        primary_subscription_id =\
            dictionary.get("primary_subscription_id")\
            if dictionary.get("primary_subscription_id")\
                else APIHelper.SKIP
        primary =\
            dictionary.get("primary")\
            if "primary" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(uid,
                   scheme,
                   primary_subscription_id,
                   primary,
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
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _scheme=(
            self.scheme
            if hasattr(self, "scheme")
            else None
        )
        _primary_subscription_id=(
            self.primary_subscription_id
            if hasattr(self, "primary_subscription_id")
            else None
        )
        _primary=(
            self.primary
            if hasattr(self, "primary")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"scheme={_scheme!r}, "
            f"primary_subscription_id={_primary_subscription_id!r}, "
            f"primary={_primary!r}, "
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
        _scheme=(
            self.scheme
            if hasattr(self, "scheme")
            else None
        )
        _primary_subscription_id=(
            self.primary_subscription_id
            if hasattr(self, "primary_subscription_id")
            else None
        )
        _primary=(
            self.primary
            if hasattr(self, "primary")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"scheme={_scheme!s}, "
            f"primary_subscription_id={_primary_subscription_id!s}, "
            f"primary={_primary!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
