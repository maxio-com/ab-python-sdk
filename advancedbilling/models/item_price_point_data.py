"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ItemPricePointData(object):
    """Implementation of the 'Item Price Point Data' model.

    Attributes:
        id (int): The model property of type int.
        handle (str): The model property of type str.
        name (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "handle": "handle",
        "name": "name",
    }

    _optionals = [
        "id",
        "handle",
        "name",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        handle=APIHelper.SKIP,
        name=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ItemPricePointData instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if handle is not APIHelper.SKIP:
            self.handle = handle
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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   handle,
                   name,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"handle={_handle!r}, "
            f"name={_name!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"handle={_handle!s}, "
            f"name={_name!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
