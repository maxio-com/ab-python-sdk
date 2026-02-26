"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class UpdatePrice(object):
    """Implementation of the 'Update Price' model.

    Attributes:
        id (int): The model property of type int.
        ending_quantity (int | str | None): The model property of type int | str |
            None.
        unit_price (float | str | None): The price can contain up to 8 decimal
            places. i.e. 1.00 or 0.0012 or 0.00000065
        destroy (bool): The model property of type bool.
        starting_quantity (int | str | None): The model property of type int | str |
            None.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "ending_quantity": "ending_quantity",
        "unit_price": "unit_price",
        "destroy": "_destroy",
        "starting_quantity": "starting_quantity",
    }

    _optionals = [
        "id",
        "ending_quantity",
        "unit_price",
        "destroy",
        "starting_quantity",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        ending_quantity=APIHelper.SKIP,
        unit_price=APIHelper.SKIP,
        destroy=APIHelper.SKIP,
        starting_quantity=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a UpdatePrice instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if ending_quantity is not APIHelper.SKIP:
            self.ending_quantity = ending_quantity
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price
        if destroy is not APIHelper.SKIP:
            self.destroy = destroy
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity

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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        ending_quantity = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("UpdatePriceEndingQuantity"),
            dictionary.get("ending_quantity"),
            False)\
            if dictionary.get("ending_quantity") is not None\
            else APIHelper.SKIP
        unit_price = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("UpdatePriceUnitPrice"),
            dictionary.get("unit_price"),
            False)\
            if dictionary.get("unit_price") is not None\
            else APIHelper.SKIP
        destroy =\
            dictionary.get("_destroy")\
            if "_destroy" in dictionary.keys()\
                else APIHelper.SKIP
        starting_quantity = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("UpdatePriceStartingQuantity"),
            dictionary.get("starting_quantity"),
            False)\
            if dictionary.get("starting_quantity") is not None\
            else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   ending_quantity,
                   unit_price,
                   destroy,
                   starting_quantity,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _ending_quantity=(
            self.ending_quantity
            if hasattr(self, "ending_quantity")
            else None
        )
        _unit_price=(
            self.unit_price
            if hasattr(self, "unit_price")
            else None
        )
        _destroy=(
            self.destroy
            if hasattr(self, "destroy")
            else None
        )
        _starting_quantity=(
            self.starting_quantity
            if hasattr(self, "starting_quantity")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"ending_quantity={_ending_quantity!r}, "
            f"unit_price={_unit_price!r}, "
            f"destroy={_destroy!r}, "
            f"starting_quantity={_starting_quantity!r}, "
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
        _ending_quantity=(
            self.ending_quantity
            if hasattr(self, "ending_quantity")
            else None
        )
        _unit_price=(
            self.unit_price
            if hasattr(self, "unit_price")
            else None
        )
        _destroy=(
            self.destroy
            if hasattr(self, "destroy")
            else None
        )
        _starting_quantity=(
            self.starting_quantity
            if hasattr(self, "starting_quantity")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"ending_quantity={_ending_quantity!s}, "
            f"unit_price={_unit_price!s}, "
            f"destroy={_destroy!s}, "
            f"starting_quantity={_starting_quantity!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
