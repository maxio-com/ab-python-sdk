"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metafield_scope import (
    MetafieldScope,
)


class UpdateMetafield(object):
    """Implementation of the 'Update Metafield' model.

    Attributes:
        current_name (str): The model property of type str.
        name (str): The model property of type str.
        scope (MetafieldScope): Warning: When updating a metafield's scope attribute,
            all scope attributes must be passed. Partially complete scope attributes
            will override the existing settings.
        input_type (MetafieldInput): Indicates the type of metafield. A text
            metafield allows any string value. Dropdown and radio metafields have a
            set of values that can be selected.  Defaults to 'text'.
        enum (List[str]): Only applicable when input_type is radio or dropdown.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_name": "current_name",
        "name": "name",
        "scope": "scope",
        "input_type": "input_type",
        "enum": "enum",
    }

    _optionals = [
        "current_name",
        "name",
        "scope",
        "input_type",
        "enum",
    ]

    def __init__(
        self,
        current_name=APIHelper.SKIP,
        name=APIHelper.SKIP,
        scope=APIHelper.SKIP,
        input_type=APIHelper.SKIP,
        enum=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a UpdateMetafield instance."""
        # Initialize members of the class
        if current_name is not APIHelper.SKIP:
            self.current_name = current_name
        if name is not APIHelper.SKIP:
            self.name = name
        if scope is not APIHelper.SKIP:
            self.scope = scope
        if input_type is not APIHelper.SKIP:
            self.input_type = input_type
        if enum is not APIHelper.SKIP:
            self.enum = enum

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
        current_name =\
            dictionary.get("current_name")\
            if dictionary.get("current_name")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        scope =\
            MetafieldScope.from_dictionary(
                dictionary.get("scope"))\
                if "scope" in dictionary.keys()\
                else APIHelper.SKIP
        input_type =\
            dictionary.get("input_type")\
            if dictionary.get("input_type")\
                else APIHelper.SKIP
        enum =\
            dictionary.get("enum")\
            if dictionary.get("enum")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(current_name,
                   name,
                   scope,
                   input_type,
                   enum,
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
        _current_name=(
            self.current_name
            if hasattr(self, "current_name")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _scope=(
            self.scope
            if hasattr(self, "scope")
            else None
        )
        _input_type=(
            self.input_type
            if hasattr(self, "input_type")
            else None
        )
        _enum=(
            self.enum
            if hasattr(self, "enum")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"current_name={_current_name!r}, "
            f"name={_name!r}, "
            f"scope={_scope!r}, "
            f"input_type={_input_type!r}, "
            f"enum={_enum!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _current_name=(
            self.current_name
            if hasattr(self, "current_name")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _scope=(
            self.scope
            if hasattr(self, "scope")
            else None
        )
        _input_type=(
            self.input_type
            if hasattr(self, "input_type")
            else None
        )
        _enum=(
            self.enum
            if hasattr(self, "enum")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"current_name={_current_name!s}, "
            f"name={_name!s}, "
            f"scope={_scope!s}, "
            f"input_type={_input_type!s}, "
            f"enum={_enum!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
