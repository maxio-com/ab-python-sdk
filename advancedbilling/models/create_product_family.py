"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class CreateProductFamily(object):
    """Implementation of the 'Create Product Family' model.

    Attributes:
        name (str): The model property of type str.
        handle (str): The model property of type str.
        description (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "handle": "handle",
        "description": "description",
    }

    _optionals = [
        "handle",
        "description",
    ]

    _nullables = [
        "handle",
        "description",
    ]

    def __init__(
        self,
        name=None,
        handle=APIHelper.SKIP,
        description=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CreateProductFamily instance."""
        # Initialize members of the class
        self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if description is not APIHelper.SKIP:
            self.description = description

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
            if "handle" in dictionary.keys()\
                else APIHelper.SKIP
        description =\
            dictionary.get("description")\
            if "description" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(name,
                   handle,
                   description,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}, "
            f"handle={_handle!r}, "
            f"description={_description!r}, "
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
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}, "
            f"handle={_handle!s}, "
            f"description={_description!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
