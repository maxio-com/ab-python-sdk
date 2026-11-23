"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.clone_feature_catalog_item import (
    CloneFeatureCatalogItem,
)


class CloneComponentPricePoint(object):
    """Implementation of the 'Clone Component Price Point' model.

    Attributes:
        name (str): The model property of type str.
        handle (str): The model property of type str.
        feature_catalog_items (List[CloneFeatureCatalogItem]): The features the clone
            gets. The clone does not copy the source price point's features, so send
            every feature it should have.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "handle": "handle",
        "feature_catalog_items": "feature_catalog_items",
    }

    _optionals = [
        "handle",
        "feature_catalog_items",
    ]

    def __init__(
        self,
        name=None,
        handle=APIHelper.SKIP,
        feature_catalog_items=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CloneComponentPricePoint instance."""
        # Initialize members of the class
        self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if feature_catalog_items is not APIHelper.SKIP:
            self.feature_catalog_items = feature_catalog_items

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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        feature_catalog_items = None
        if dictionary.get("feature_catalog_items") is not None:
            feature_catalog_items = [
                CloneFeatureCatalogItem.from_dictionary(x)
                    for x in dictionary.get("feature_catalog_items")
            ]
        else:
            feature_catalog_items = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(name,
                   handle,
                   feature_catalog_items,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _feature_catalog_items=(
            self.feature_catalog_items
            if hasattr(self, "feature_catalog_items")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}, "
            f"handle={_handle!r}, "
            f"feature_catalog_items={_feature_catalog_items!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=self.name
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _feature_catalog_items=(
            self.feature_catalog_items
            if hasattr(self, "feature_catalog_items")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}, "
            f"handle={_handle!s}, "
            f"feature_catalog_items={_feature_catalog_items!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
