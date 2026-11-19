"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Wallet2(object):
    """Implementation of the 'Wallet2' model.

    Attributes:
        name (str): A merchant-facing label for the wallet. Surrounding spaces are
            stripped; a blank or `null` value clears it.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
    }

    _optionals = [
        "name",
    ]

    _nullables = [
        "name",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Wallet2 instance."""
        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name

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
            if "name" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(name,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
