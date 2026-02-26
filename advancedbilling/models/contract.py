"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.register import (
    Register,
)


class Contract(object):
    """Implementation of the 'Contract' model.

    Contract linked to the scheduled renewal configuration.

    Attributes:
        id (int): The model property of type int.
        maxio_id (str): The model property of type str.
        number (str): The model property of type str.
        register (Register): The model property of type Register.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "maxio_id": "maxio_id",
        "number": "number",
        "register": "register",
    }

    _optionals = [
        "id",
        "maxio_id",
        "number",
        "register",
    ]

    _nullables = [
        "number",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        maxio_id=APIHelper.SKIP,
        number=APIHelper.SKIP,
        register=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Contract instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if maxio_id is not APIHelper.SKIP:
            self.maxio_id = maxio_id
        if number is not APIHelper.SKIP:
            self.number = number
        if register is not APIHelper.SKIP:
            self.register = register

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
        maxio_id =\
            dictionary.get("maxio_id")\
            if dictionary.get("maxio_id")\
                else APIHelper.SKIP
        number =\
            dictionary.get("number")\
            if "number" in dictionary.keys()\
                else APIHelper.SKIP
        register =\
            Register.from_dictionary(
                dictionary.get("register"))\
                if "register" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   maxio_id,
                   number,
                   register,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _maxio_id=(
            self.maxio_id
            if hasattr(self, "maxio_id")
            else None
        )
        _number=(
            self.number
            if hasattr(self, "number")
            else None
        )
        _register=(
            self.register
            if hasattr(self, "register")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"maxio_id={_maxio_id!r}, "
            f"number={_number!r}, "
            f"register={_register!r}, "
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
        _maxio_id=(
            self.maxio_id
            if hasattr(self, "maxio_id")
            else None
        )
        _number=(
            self.number
            if hasattr(self, "number")
            else None
        )
        _register=(
            self.register
            if hasattr(self, "register")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"maxio_id={_maxio_id!s}, "
            f"number={_number!s}, "
            f"register={_register!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
