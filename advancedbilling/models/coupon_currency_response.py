"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.coupon_currency import (
    CouponCurrency,
)


class CouponCurrencyResponse(object):
    """Implementation of the 'Coupon Currency Response' model.

    Attributes:
        currency_prices (List[CouponCurrency]): The model property of type
            List[CouponCurrency].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency_prices": "currency_prices",
    }

    _optionals = [
        "currency_prices",
    ]

    def __init__(
        self,
        currency_prices=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CouponCurrencyResponse instance."""
        # Initialize members of the class
        if currency_prices is not APIHelper.SKIP:
            self.currency_prices = currency_prices

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
        currency_prices = None
        if dictionary.get("currency_prices") is not None:
            currency_prices = [
                CouponCurrency.from_dictionary(x)
                    for x in dictionary.get("currency_prices")
            ]
        else:
            currency_prices = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(currency_prices,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _currency_prices=(
            self.currency_prices
            if hasattr(self, "currency_prices")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currency_prices={_currency_prices!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _currency_prices=(
            self.currency_prices
            if hasattr(self, "currency_prices")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currency_prices={_currency_prices!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
