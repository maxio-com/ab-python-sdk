"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Errors(object):
    """Implementation of the 'Errors' model.

    Attributes:
        per_page (List[str]): The model property of type List[str].
        price_point (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "per_page": "per_page",
        "price_point": "price_point",
    }

    _optionals = [
        "per_page",
        "price_point",
    ]

    def __init__(
        self,
        per_page=APIHelper.SKIP,
        price_point=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Errors instance."""
        # Initialize members of the class
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page
        if price_point is not APIHelper.SKIP:
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
        per_page =\
            dictionary.get("per_page")\
            if dictionary.get("per_page")\
                else APIHelper.SKIP
        price_point =\
            dictionary.get("price_point")\
            if dictionary.get("price_point")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(per_page,
                   price_point,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _per_page=(
            self.per_page
            if hasattr(self, "per_page")
            else None
        )
        _price_point=(
            self.price_point
            if hasattr(self, "price_point")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"per_page={_per_page!r}, "
            f"price_point={_price_point!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _per_page=(
            self.per_page
            if hasattr(self, "per_page")
            else None
        )
        _price_point=(
            self.price_point
            if hasattr(self, "price_point")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"per_page={_per_page!s}, "
            f"price_point={_price_point!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
