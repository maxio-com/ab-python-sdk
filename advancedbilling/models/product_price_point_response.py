"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.product_price_point import (
    ProductPricePoint,
)


class ProductPricePointResponse(object):
    """Implementation of the 'Product Price Point Response' model.

    Attributes:
        price_point (ProductPricePoint): The model property of type ProductPricePoint.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_point": "price_point",
    }

    def __init__(
        self,
        price_point=None,
        additional_properties=None):
        """Initialize a ProductPricePointResponse instance."""
        # Initialize members of the class
        self.price_point = price_point

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
        price_point =\
            ProductPricePoint.from_dictionary(
                dictionary.get("price_point"))\
                if dictionary.get("price_point") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(price_point,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _price_point=self.price_point
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"price_point={_price_point!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _price_point=self.price_point
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"price_point={_price_point!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
