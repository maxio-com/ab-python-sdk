"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Meter(object):
    """Implementation of the 'Meter' model.

    The metering meter this wallet is paired with, or `null` for a wallet with no
    meter. Set on create and immutable afterward.

    Attributes:
        id (int): The model property of type int.
        name (str): The model property of type str.
        handle (str): The model property of type str.
        conversion_rate (str): How many wallet units one meter unit is worth, as a
            decimal string. Defaults to `"1.0"`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "name": "name",
        "handle": "handle",
        "conversion_rate": "conversion_rate",
    }

    _optionals = [
        "id",
        "name",
        "handle",
        "conversion_rate",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        handle=APIHelper.SKIP,
        conversion_rate=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Meter instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if conversion_rate is not APIHelper.SKIP:
            self.conversion_rate = conversion_rate

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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        conversion_rate =\
            dictionary.get("conversion_rate")\
            if dictionary.get("conversion_rate")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   name,
                   handle,
                   conversion_rate,
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
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _conversion_rate=(
            self.conversion_rate
            if hasattr(self, "conversion_rate")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"name={_name!r}, "
            f"handle={_handle!r}, "
            f"conversion_rate={_conversion_rate!r}, "
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
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _conversion_rate=(
            self.conversion_rate
            if hasattr(self, "conversion_rate")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"name={_name!s}, "
            f"handle={_handle!s}, "
            f"conversion_rate={_conversion_rate!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
