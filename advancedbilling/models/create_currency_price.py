"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class CreateCurrencyPrice(object):
    """Implementation of the 'Create Currency Price' model.

    Attributes:
        currency (str): ISO code for a currency defined on the site level
        price (float): Price for the price level in this currency
        price_id (int): ID of the price that this corresponds with
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": "currency",
        "price": "price",
        "price_id": "price_id",
    }

    _optionals = [
        "currency",
        "price",
        "price_id",
    ]

    def __init__(
        self,
        currency=APIHelper.SKIP,
        price=APIHelper.SKIP,
        price_id=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CreateCurrencyPrice instance."""
        # Initialize members of the class
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if price is not APIHelper.SKIP:
            self.price = price
        if price_id is not APIHelper.SKIP:
            self.price_id = price_id

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
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        price =\
            dictionary.get("price")\
            if dictionary.get("price")\
                else APIHelper.SKIP
        price_id =\
            dictionary.get("price_id")\
            if dictionary.get("price_id")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(currency,
                   price,
                   price_id,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
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
        _price_id=(
            self.price_id
            if hasattr(self, "price_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currency={_currency!r}, "
            f"price={_price!r}, "
            f"price_id={_price_id!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
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
        _price_id=(
            self.price_id
            if hasattr(self, "price_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currency={_currency!s}, "
            f"price={_price!s}, "
            f"price_id={_price_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
