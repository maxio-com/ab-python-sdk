"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ComponentCurrencyPrice(object):
    """Implementation of the 'Component Currency Price' model.

    Attributes:
        id (int): The model property of type int.
        currency (str): The model property of type str.
        price (str): The model property of type str.
        formatted_price (str): The model property of type str.
        price_id (int): The model property of type int.
        price_point_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "currency": "currency",
        "price": "price",
        "formatted_price": "formatted_price",
        "price_id": "price_id",
        "price_point_id": "price_point_id",
    }

    _optionals = [
        "id",
        "currency",
        "price",
        "formatted_price",
        "price_id",
        "price_point_id",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        price=APIHelper.SKIP,
        formatted_price=APIHelper.SKIP,
        price_id=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ComponentCurrencyPrice instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if price is not APIHelper.SKIP:
            self.price = price
        if formatted_price is not APIHelper.SKIP:
            self.formatted_price = formatted_price
        if price_id is not APIHelper.SKIP:
            self.price_id = price_id
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id

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
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        price =\
            dictionary.get("price")\
            if dictionary.get("price")\
                else APIHelper.SKIP
        formatted_price =\
            dictionary.get("formatted_price")\
            if dictionary.get("formatted_price")\
                else APIHelper.SKIP
        price_id =\
            dictionary.get("price_id")\
            if dictionary.get("price_id")\
                else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   currency,
                   price,
                   formatted_price,
                   price_id,
                   price_point_id,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _price=(
            self.price
            if hasattr(self, "price")
            else None
        )
        _formatted_price=(
            self.formatted_price
            if hasattr(self, "formatted_price")
            else None
        )
        _price_id=(
            self.price_id
            if hasattr(self, "price_id")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"currency={_currency!r}, "
            f"price={_price!r}, "
            f"formatted_price={_formatted_price!r}, "
            f"price_id={_price_id!r}, "
            f"price_point_id={_price_point_id!r}, "
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
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _price=(
            self.price
            if hasattr(self, "price")
            else None
        )
        _formatted_price=(
            self.formatted_price
            if hasattr(self, "formatted_price")
            else None
        )
        _price_id=(
            self.price_id
            if hasattr(self, "price_id")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"currency={_currency!s}, "
            f"price={_price!s}, "
            f"formatted_price={_formatted_price!s}, "
            f"price_id={_price_id!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
