"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.feature_catalog_item import (
    FeatureCatalogItem,
)


class FeatureCatalogItemsListResponse(object):
    """Implementation of the 'Feature Catalog Items List Response' model.

    Attributes:
        features (List[FeatureCatalogItem]): The model property of type
            List[FeatureCatalogItem].
        subscriptions_count (int): The number of subscriptions on this
            product/component that would be affected if a feature catalog item change
            were propagated with `propagate_to_subscriptions=true`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "features": "features",
        "subscriptions_count": "subscriptions_count",
    }

    def __init__(
        self,
        features=None,
        subscriptions_count=None,
        additional_properties=None):
        """Initialize a FeatureCatalogItemsListResponse instance."""
        # Initialize members of the class
        self.features = features
        self.subscriptions_count = subscriptions_count

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
        features = None
        if dictionary.get("features") is not None:
            features = [
                FeatureCatalogItem.from_dictionary(x)
                    for x in dictionary.get("features")
            ]
        subscriptions_count =\
            dictionary.get("subscriptions_count")\
            if dictionary.get("subscriptions_count")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(features,
                   subscriptions_count,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _features=self.features
        _subscriptions_count=self.subscriptions_count
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"features={_features!r}, "
            f"subscriptions_count={_subscriptions_count!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _features=self.features
        _subscriptions_count=self.subscriptions_count
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"features={_features!s}, "
            f"subscriptions_count={_subscriptions_count!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
