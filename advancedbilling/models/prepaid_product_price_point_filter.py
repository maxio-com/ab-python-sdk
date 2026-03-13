"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class PrepaidProductPricePointFilter(object):
    """Implementation of the 'Prepaid Product Price Point Filter' model.

    Attributes:
        product_price_point_id (str): Passed as a parameter to list methods to return
            only non null values.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_price_point_id": "product_price_point_id",
    }

    def __init__(
        self,
        additional_properties=None):
        """Initialize a PrepaidProductPricePointFilter instance."""
        # Initialize members of the class
        self.product_price_point_id = "not_null"

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

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _product_price_point_id=self.product_price_point_id
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"product_price_point_id={_product_price_point_id!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _product_price_point_id=self.product_price_point_id
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"product_price_point_id={_product_price_point_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
