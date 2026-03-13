"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.product_price_point import (
    ProductPricePoint,
)


class BulkCreateProductPricePointsResponse(object):
    """Implementation of the 'Bulk Create Product Price Points Response' model.

    Attributes:
        price_points (List[ProductPricePoint]): The model property of type
            List[ProductPricePoint].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_points": "price_points",
    }

    _optionals = [
        "price_points",
    ]

    def __init__(
        self,
        price_points=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BulkCreateProductPricePointsResponse instance."""
        # Initialize members of the class
        if price_points is not APIHelper.SKIP:
            self.price_points = price_points

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
        price_points = None
        if dictionary.get("price_points") is not None:
            price_points = [
                ProductPricePoint.from_dictionary(x)
                    for x in dictionary.get("price_points")
            ]
        else:
            price_points = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(price_points,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _price_points=(
            self.price_points
            if hasattr(self, "price_points")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"price_points={_price_points!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _price_points=(
            self.price_points
            if hasattr(self, "price_points")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"price_points={_price_points!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
