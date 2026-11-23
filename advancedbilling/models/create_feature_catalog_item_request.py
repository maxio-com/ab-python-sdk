"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.feature_2 import (
    Feature2,
)


class CreateFeatureCatalogItemRequest(object):
    """Implementation of the 'Create Feature Catalog Item Request' model.

    The owning product or component is taken from the URL and must not be included in
    the request body.

    Attributes:
        feature (Feature2): The model property of type Feature2.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature": "feature",
    }

    def __init__(
        self,
        feature=None,
        additional_properties=None):
        """Initialize a CreateFeatureCatalogItemRequest instance."""
        # Initialize members of the class
        self.feature = feature

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
        feature =\
            Feature2.from_dictionary(
                dictionary.get("feature"))\
                if dictionary.get("feature") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(feature,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _feature=self.feature
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature={_feature!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _feature=self.feature
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature={_feature!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
