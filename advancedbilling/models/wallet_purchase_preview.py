"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class WalletPurchasePreview(object):
    """Implementation of the 'Wallet Purchase Preview' model.

    A price quote for a purchase, without charging anything.

    Attributes:
        price_point_id (int): The model property of type int.
        currency (str): The three-letter currency code the `amount` is denominated
            in, matching the subscription's currency.
        quantity (str): The number of units the quote is for, as a decimal string.
        amount (str): The price for `quantity` units at this price point, as a
            decimal string.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_point_id": "price_point_id",
        "currency": "currency",
        "quantity": "quantity",
        "amount": "amount",
    }

    def __init__(
        self,
        price_point_id=None,
        currency=None,
        quantity=None,
        amount=None,
        additional_properties=None):
        """Initialize a WalletPurchasePreview instance."""
        # Initialize members of the class
        self.price_point_id = price_point_id
        self.currency = currency
        self.quantity = quantity
        self.amount = amount

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
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else None
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else None
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else None
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(price_point_id,
                   currency,
                   quantity,
                   amount,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _price_point_id=self.price_point_id
        _currency=self.currency
        _quantity=self.quantity
        _amount=self.amount
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"price_point_id={_price_point_id!r}, "
            f"currency={_currency!r}, "
            f"quantity={_quantity!r}, "
            f"amount={_amount!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _price_point_id=self.price_point_id
        _currency=self.currency
        _quantity=self.quantity
        _amount=self.amount
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"price_point_id={_price_point_id!s}, "
            f"currency={_currency!s}, "
            f"quantity={_quantity!s}, "
            f"amount={_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
