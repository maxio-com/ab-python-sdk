"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Endpoint(object):
    """Implementation of the 'Endpoint' model.

    Attributes:
        id (int): The model property of type int.
        url (str): The model property of type str.
        site_id (int): The model property of type int.
        status (str): The model property of type str.
        webhook_subscriptions (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "url": "url",
        "site_id": "site_id",
        "status": "status",
        "webhook_subscriptions": "webhook_subscriptions",
    }

    _optionals = [
        "id",
        "url",
        "site_id",
        "status",
        "webhook_subscriptions",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        url=APIHelper.SKIP,
        site_id=APIHelper.SKIP,
        status=APIHelper.SKIP,
        webhook_subscriptions=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Endpoint instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if url is not APIHelper.SKIP:
            self.url = url
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id
        if status is not APIHelper.SKIP:
            self.status = status
        if webhook_subscriptions is not APIHelper.SKIP:
            self.webhook_subscriptions = webhook_subscriptions

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
        url =\
            dictionary.get("url")\
            if dictionary.get("url")\
                else APIHelper.SKIP
        site_id =\
            dictionary.get("site_id")\
            if dictionary.get("site_id")\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        webhook_subscriptions =\
            dictionary.get("webhook_subscriptions")\
            if dictionary.get("webhook_subscriptions")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   url,
                   site_id,
                   status,
                   webhook_subscriptions,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _url=(
            self.url
            if hasattr(self, "url")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _webhook_subscriptions=(
            self.webhook_subscriptions
            if hasattr(self, "webhook_subscriptions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"url={_url!r}, "
            f"site_id={_site_id!r}, "
            f"status={_status!r}, "
            f"webhook_subscriptions={_webhook_subscriptions!r}, "
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
        _url=(
            self.url
            if hasattr(self, "url")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _webhook_subscriptions=(
            self.webhook_subscriptions
            if hasattr(self, "webhook_subscriptions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"url={_url!s}, "
            f"site_id={_site_id!s}, "
            f"status={_status!s}, "
            f"webhook_subscriptions={_webhook_subscriptions!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
