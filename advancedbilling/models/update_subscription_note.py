"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class UpdateSubscriptionNote(object):
    """Implementation of the 'Update Subscription Note' model.

    Updatable fields for Subscription Note

    Attributes:
        body (str): The model property of type str.
        sticky (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body": "body",
        "sticky": "sticky",
    }

    def __init__(
        self,
        body=None,
        sticky=None,
        additional_properties=None):
        """Initialize a UpdateSubscriptionNote instance."""
        # Initialize members of the class
        self.body = body
        self.sticky = sticky

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
        body =\
            dictionary.get("body")\
            if dictionary.get("body")\
                else None
        sticky =\
            dictionary.get("sticky")\
            if "sticky" in dictionary.keys()\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(body,
                   sticky,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _body=self.body
        _sticky=self.sticky
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"body={_body!r}, "
            f"sticky={_sticky!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _body=self.body
        _sticky=self.sticky
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"body={_body!s}, "
            f"sticky={_sticky!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
