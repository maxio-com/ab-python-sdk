"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.update_component import (
    UpdateComponent,
)


class UpdateComponentRequest(object):
    """Implementation of the 'Update Component Request' model.

    Attributes:
        component (UpdateComponent): The model property of type UpdateComponent.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component": "component",
    }

    def __init__(
        self,
        component=None,
        additional_properties=None):
        """Initialize a UpdateComponentRequest instance."""
        # Initialize members of the class
        self.component = component

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
        component =\
            UpdateComponent.from_dictionary(
                dictionary.get("component"))\
                if dictionary.get("component") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(component,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _component=self.component
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"component={_component!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _component=self.component
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"component={_component!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
