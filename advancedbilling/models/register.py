"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Register(object):
    """Implementation of the 'Register' model.

    Attributes:
        id (int): The model property of type int.
        maxio_id (str): The model property of type str.
        name (str): The model property of type str.
        currency_code (str): The ISO 4217 currency code (3 character string)
            representing the currency of invoice transaction.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "maxio_id": "maxio_id",
        "name": "name",
        "currency_code": "currency_code",
    }

    _optionals = [
        "id",
        "maxio_id",
        "name",
        "currency_code",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        maxio_id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        currency_code=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Register instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if maxio_id is not APIHelper.SKIP:
            self.maxio_id = maxio_id
        if name is not APIHelper.SKIP:
            self.name = name
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code

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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        currency_code =\
            dictionary.get("currency_code")\
            if dictionary.get("currency_code")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   maxio_id,
                   name,
                   currency_code,
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _currency_code=(
            self.currency_code
            if hasattr(self, "currency_code")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"maxio_id={_maxio_id!r}, "
            f"name={_name!r}, "
            f"currency_code={_currency_code!r}, "
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _currency_code=(
            self.currency_code
            if hasattr(self, "currency_code")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"maxio_id={_maxio_id!s}, "
            f"name={_name!s}, "
            f"currency_code={_currency_code!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
