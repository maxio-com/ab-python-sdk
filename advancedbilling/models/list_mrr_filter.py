"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ListMrrFilter(object):
    """Implementation of the 'List Mrr Filter' model.

    Attributes:
        subscription_ids (List[int]): Submit ids in order to limit results. Use in
            query: `filter[subscription_ids]=1,2,3`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_ids": "subscription_ids",
    }

    _optionals = [
        "subscription_ids",
    ]

    def __init__(
        self,
        subscription_ids=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ListMrrFilter instance."""
        # Initialize members of the class
        if subscription_ids is not APIHelper.SKIP:
            self.subscription_ids = subscription_ids

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
        subscription_ids =\
            dictionary.get("subscription_ids")\
            if dictionary.get("subscription_ids")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(subscription_ids,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _subscription_ids=(
            self.subscription_ids
            if hasattr(self, "subscription_ids")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription_ids={_subscription_ids!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _subscription_ids=(
            self.subscription_ids
            if hasattr(self, "subscription_ids")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription_ids={_subscription_ids!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
