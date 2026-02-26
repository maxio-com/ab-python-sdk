"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class CouponRestriction(object):
    """Implementation of the 'Coupon Restriction' model.

    Attributes:
        id (int): The model property of type int.
        item_type (RestrictionType): The model property of type RestrictionType.
        item_id (int): The model property of type int.
        name (str): The model property of type str.
        handle (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "item_type": "item_type",
        "item_id": "item_id",
        "name": "name",
        "handle": "handle",
    }

    _optionals = [
        "id",
        "item_type",
        "item_id",
        "name",
        "handle",
    ]

    _nullables = [
        "handle",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        item_type=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        handle=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CouponRestriction instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if item_type is not APIHelper.SKIP:
            self.item_type = item_type
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if name is not APIHelper.SKIP:
            self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle

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
        item_type =\
            dictionary.get("item_type")\
            if dictionary.get("item_type")\
                else APIHelper.SKIP
        item_id =\
            dictionary.get("item_id")\
            if dictionary.get("item_id")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        handle =\
            dictionary.get("handle")\
            if "handle" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   item_type,
                   item_id,
                   name,
                   handle,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _item_type=(
            self.item_type
            if hasattr(self, "item_type")
            else None
        )
        _item_id=(
            self.item_id
            if hasattr(self, "item_id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"item_type={_item_type!r}, "
            f"item_id={_item_id!r}, "
            f"name={_name!r}, "
            f"handle={_handle!r}, "
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
        _item_type=(
            self.item_type
            if hasattr(self, "item_type")
            else None
        )
        _item_id=(
            self.item_id
            if hasattr(self, "item_id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"item_type={_item_type!s}, "
            f"item_id={_item_id!s}, "
            f"name={_name!s}, "
            f"handle={_handle!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
