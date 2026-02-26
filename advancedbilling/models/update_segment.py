"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_or_update_segment_price import (
    CreateOrUpdateSegmentPrice,
)


class UpdateSegment(object):
    """Implementation of the 'Update Segment' model.

    Attributes:
        pricing_scheme (PricingScheme): The identifier for the pricing scheme. See
            [Product
            Components](https://help.chargify.com/products/product-components.html)
            for an overview of pricing schemes.
        prices (List[CreateOrUpdateSegmentPrice]): The model property of type
            List[CreateOrUpdateSegmentPrice].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": "pricing_scheme",
        "prices": "prices",
    }

    _optionals = [
        "prices",
    ]

    def __init__(
        self,
        pricing_scheme=None,
        prices=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a UpdateSegment instance."""
        # Initialize members of the class
        self.pricing_scheme = pricing_scheme
        if prices is not APIHelper.SKIP:
            self.prices = prices

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
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if dictionary.get("pricing_scheme")\
                else None
        prices = None
        if dictionary.get("prices") is not None:
            prices = [
                CreateOrUpdateSegmentPrice.from_dictionary(x)
                    for x in dictionary.get("prices")
            ]
        else:
            prices = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(pricing_scheme,
                   prices,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _pricing_scheme=self.pricing_scheme
        _prices=(
            self.prices
            if hasattr(self, "prices")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"pricing_scheme={_pricing_scheme!r}, "
            f"prices={_prices!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _pricing_scheme=self.pricing_scheme
        _prices=(
            self.prices
            if hasattr(self, "prices")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"pricing_scheme={_pricing_scheme!s}, "
            f"prices={_prices!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
