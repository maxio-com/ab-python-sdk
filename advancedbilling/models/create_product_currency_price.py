"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class CreateProductCurrencyPrice(object):
    """Implementation of the 'Create Product Currency Price' model.

    Attributes:
        currency (str): ISO code for one of the site level currencies.
        price (int): Price for the given role.
        role (CurrencyPriceRole): Role for the price.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": "currency",
        "price": "price",
        "role": "role",
    }

    def __init__(
        self,
        currency=None,
        price=None,
        role=None,
        additional_properties=None):
        """Initialize a CreateProductCurrencyPrice instance."""
        # Initialize members of the class
        self.currency = currency
        self.price = price
        self.role = role

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
                else None
        price =\
            dictionary.get("price")\
            if dictionary.get("price")\
                else None
        role =\
            dictionary.get("role")\
            if dictionary.get("role")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(currency,
                   price,
                   role,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _currency=self.currency
        _price=self.price
        _role=self.role
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currency={_currency!r}, "
            f"price={_price!r}, "
            f"role={_role!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _currency=self.currency
        _price=self.price
        _role=self.role
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currency={_currency!s}, "
            f"price={_price!s}, "
            f"role={_role!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
