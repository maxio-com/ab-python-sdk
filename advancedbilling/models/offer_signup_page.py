"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class OfferSignupPage(object):
    """Implementation of the 'Offer Signup Page' model.

    Attributes:
        id (int): The model property of type int.
        nickname (str): The model property of type str.
        enabled (bool): The model property of type bool.
        return_url (str): The model property of type str.
        return_params (str): The model property of type str.
        url (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "nickname": "nickname",
        "enabled": "enabled",
        "return_url": "return_url",
        "return_params": "return_params",
        "url": "url",
    }

    _optionals = [
        "id",
        "nickname",
        "enabled",
        "return_url",
        "return_params",
        "url",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        nickname=APIHelper.SKIP,
        enabled=APIHelper.SKIP,
        return_url=APIHelper.SKIP,
        return_params=APIHelper.SKIP,
        url=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a OfferSignupPage instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if nickname is not APIHelper.SKIP:
            self.nickname = nickname
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if return_url is not APIHelper.SKIP:
            self.return_url = return_url
        if return_params is not APIHelper.SKIP:
            self.return_params = return_params
        if url is not APIHelper.SKIP:
            self.url = url

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
        nickname =\
            dictionary.get("nickname")\
            if dictionary.get("nickname")\
                else APIHelper.SKIP
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        return_url =\
            dictionary.get("return_url")\
            if dictionary.get("return_url")\
                else APIHelper.SKIP
        return_params =\
            dictionary.get("return_params")\
            if dictionary.get("return_params")\
                else APIHelper.SKIP
        url =\
            dictionary.get("url")\
            if dictionary.get("url")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   nickname,
                   enabled,
                   return_url,
                   return_params,
                   url,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _nickname=(
            self.nickname
            if hasattr(self, "nickname")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _return_url=(
            self.return_url
            if hasattr(self, "return_url")
            else None
        )
        _return_params=(
            self.return_params
            if hasattr(self, "return_params")
            else None
        )
        _url=(
            self.url
            if hasattr(self, "url")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"nickname={_nickname!r}, "
            f"enabled={_enabled!r}, "
            f"return_url={_return_url!r}, "
            f"return_params={_return_params!r}, "
            f"url={_url!r}, "
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
        _nickname=(
            self.nickname
            if hasattr(self, "nickname")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _return_url=(
            self.return_url
            if hasattr(self, "return_url")
            else None
        )
        _return_params=(
            self.return_params
            if hasattr(self, "return_params")
            else None
        )
        _url=(
            self.url
            if hasattr(self, "url")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"nickname={_nickname!s}, "
            f"enabled={_enabled!s}, "
            f"return_url={_return_url!s}, "
            f"return_params={_return_params!s}, "
            f"url={_url!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
