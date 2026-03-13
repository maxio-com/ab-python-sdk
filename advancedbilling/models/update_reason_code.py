"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class UpdateReasonCode(object):
    """Implementation of the 'Update Reason Code' model.

    Attributes:
        code (str): The unique identifier for the ReasonCode
        description (str): The friendly summary of what the code signifies
        position (int): The order that code appears in lists
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": "code",
        "description": "description",
        "position": "position",
    }

    _optionals = [
        "code",
        "description",
        "position",
    ]

    def __init__(
        self,
        code=APIHelper.SKIP,
        description=APIHelper.SKIP,
        position=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a UpdateReasonCode instance."""
        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code
        if description is not APIHelper.SKIP:
            self.description = description
        if position is not APIHelper.SKIP:
            self.position = position

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
        code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else APIHelper.SKIP
        description =\
            dictionary.get("description")\
            if dictionary.get("description")\
                else APIHelper.SKIP
        position =\
            dictionary.get("position")\
            if dictionary.get("position")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(code,
                   description,
                   position,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _position=(
            self.position
            if hasattr(self, "position")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!r}, "
            f"description={_description!r}, "
            f"position={_position!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _position=(
            self.position
            if hasattr(self, "position")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!s}, "
            f"description={_description!s}, "
            f"position={_position!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
