"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ListSubscriptionGroupsMeta(object):
    """Implementation of the 'List Subscription Groups Meta' model.

    Attributes:
        current_page (int): The model property of type int.
        total_count (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_page": "current_page",
        "total_count": "total_count",
    }

    _optionals = [
        "current_page",
        "total_count",
    ]

    def __init__(
        self,
        current_page=APIHelper.SKIP,
        total_count=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ListSubscriptionGroupsMeta instance."""
        # Initialize members of the class
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count

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
        current_page =\
            dictionary.get("current_page")\
            if dictionary.get("current_page")\
                else APIHelper.SKIP
        total_count =\
            dictionary.get("total_count")\
            if dictionary.get("total_count")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(current_page,
                   total_count,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _current_page=(
            self.current_page
            if hasattr(self, "current_page")
            else None
        )
        _total_count=(
            self.total_count
            if hasattr(self, "total_count")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"current_page={_current_page!r}, "
            f"total_count={_total_count!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _current_page=(
            self.current_page
            if hasattr(self, "current_page")
            else None
        )
        _total_count=(
            self.total_count
            if hasattr(self, "total_count")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"current_page={_current_page!s}, "
            f"total_count={_total_count!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
