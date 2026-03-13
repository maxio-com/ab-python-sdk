"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.site import Site


class SiteResponse(object):
    """Implementation of the 'Site Response' model.

    Attributes:
        site (Site): The model property of type Site.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "site": "site",
    }

    def __init__(
        self,
        site=None,
        additional_properties=None):
        """Initialize a SiteResponse instance."""
        # Initialize members of the class
        self.site = site

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
        site =\
            Site.from_dictionary(
                dictionary.get("site"))\
                if dictionary.get("site") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(site,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _site=self.site
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"site={_site!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _site=self.site
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"site={_site!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
