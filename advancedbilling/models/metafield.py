"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metafield_scope import (
    MetafieldScope,
)


class Metafield(object):
    """Implementation of the 'Metafield' model.

    Attributes:
        id (int): The model property of type int.
        name (str): The model property of type str.
        scope (MetafieldScope): Warning: When updating a metafield's scope attribute,
            all scope attributes must be passed. Partially complete scope attributes
            will override the existing settings.
        data_count (int): The amount of subscriptions this metafield has been applied
            to in Advanced Billing.
        input_type (MetafieldInput): Indicates the type of metafield. A text
            metafield allows any string value. Dropdown and radio metafields have a
            set of values that can be selected.  Defaults to 'text'.
        enum (str | List[str] | None): The model property of type str | List[str] |
            None.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "name": "name",
        "scope": "scope",
        "data_count": "data_count",
        "input_type": "input_type",
        "enum": "enum",
    }

    _optionals = [
        "id",
        "name",
        "scope",
        "data_count",
        "input_type",
        "enum",
    ]

    _nullables = [
        "enum",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        scope=APIHelper.SKIP,
        data_count=APIHelper.SKIP,
        input_type=APIHelper.SKIP,
        enum=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Metafield instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if scope is not APIHelper.SKIP:
            self.scope = scope
        if data_count is not APIHelper.SKIP:
            self.data_count = data_count
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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
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
        data_count =\
            dictionary.get("data_count")\
            if dictionary.get("data_count")\
                else APIHelper.SKIP
        input_type =\
            dictionary.get("input_type")\
            if dictionary.get("input_type")\
                else APIHelper.SKIP
        if "enum" in dictionary.keys():
            enum = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("MetafieldEnum"),
            dictionary.get("enum"),
            False)\
            if dictionary.get("enum") is not None\
            else None
        else:
            enum = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   name,
                   scope,
                   data_count,
                   input_type,
                   enum,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
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
        _data_count=(
            self.data_count
            if hasattr(self, "data_count")
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
            f"id={_id!r}, "
            f"name={_name!r}, "
            f"scope={_scope!r}, "
            f"data_count={_data_count!r}, "
            f"input_type={_input_type!r}, "
            f"enum={_enum!r}, "
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
        _data_count=(
            self.data_count
            if hasattr(self, "data_count")
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
            f"id={_id!s}, "
            f"name={_name!s}, "
            f"scope={_scope!s}, "
            f"data_count={_data_count!s}, "
            f"input_type={_input_type!s}, "
            f"enum={_enum!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
