"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class UpdateCurrencyPrice(object):
    """Implementation of the 'Update Currency Price' model.

    Attributes:
        id (int): ID of the currency price record being updated
        price (float): New price for the given currency
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "price": "price",
    }

    def __init__(
        self,
        id=None,
        price=None,
        additional_properties=None):
        """Initialize a UpdateCurrencyPrice instance."""
        # Initialize members of the class
        self.id = id
        self.price = price

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
                else None
        price =\
            dictionary.get("price")\
            if dictionary.get("price")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   price,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=self.id
        _price=self.price
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"price={_price!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=self.id
        _price=self.price
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"price={_price!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
