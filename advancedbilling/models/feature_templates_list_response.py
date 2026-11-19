"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.feature_template import (
    FeatureTemplate,
)


class FeatureTemplatesListResponse(object):
    """Implementation of the 'Feature Templates List Response' model.

    Attributes:
        items (List[FeatureTemplate]): The model property of type
            List[FeatureTemplate].
        total_count (int): Total number of feature templates matching the filters,
            across all pages.
        archived_count (int): Number of archived feature templates matching the
            filters. Returned as `0` unless the active result set is empty or
            `status=archived` was requested.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items": "items",
        "total_count": "total_count",
        "archived_count": "archived_count",
    }

    def __init__(
        self,
        items=None,
        total_count=None,
        archived_count=None,
        additional_properties=None):
        """Initialize a FeatureTemplatesListResponse instance."""
        # Initialize members of the class
        self.items = items
        self.total_count = total_count
        self.archived_count = archived_count

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
        items = None
        if dictionary.get("items") is not None:
            items = [
                FeatureTemplate.from_dictionary(x)
                    for x in dictionary.get("items")
            ]
        total_count =\
            dictionary.get("total_count")\
            if dictionary.get("total_count")\
                else None
        archived_count =\
            dictionary.get("archived_count")\
            if dictionary.get("archived_count")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(items,
                   total_count,
                   archived_count,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _items=self.items
        _total_count=self.total_count
        _archived_count=self.archived_count
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"items={_items!r}, "
            f"total_count={_total_count!r}, "
            f"archived_count={_archived_count!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _items=self.items
        _total_count=self.total_count
        _archived_count=self.archived_count
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"items={_items!s}, "
            f"total_count={_total_count!s}, "
            f"archived_count={_archived_count!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
