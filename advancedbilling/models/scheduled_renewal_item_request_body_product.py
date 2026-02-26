"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.scheduled_renewal_product_price_point import (
    ScheduledRenewalProductPricePoint,
)


class ScheduledRenewalItemRequestBodyProduct(object):
    """Implementation of the 'Scheduled Renewal Item Request Body Product' model.

    Attributes:
        item_type (str): Item type to add. Either Product or Component.
        item_id (int): Product or component identifier.
        price_point_id (int): Price point identifier.
        quantity (int): Optional quantity for the item.
        custom_price (ScheduledRenewalProductPricePoint): Custom pricing for a
            product within a scheduled renewal.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item_type": "item_type",
        "item_id": "item_id",
        "price_point_id": "price_point_id",
        "quantity": "quantity",
        "custom_price": "custom_price",
    }

    _optionals = [
        "price_point_id",
        "quantity",
        "custom_price",
    ]

    def __init__(
        self,
        item_id=None,
        price_point_id=APIHelper.SKIP,
        quantity=APIHelper.SKIP,
        custom_price=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalItemRequestBodyProduct instance."""
        # Initialize members of the class
        self.item_type = "Product"
        self.item_id = item_id
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price

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
        item_id =\
            dictionary.get("item_id")\
            if dictionary.get("item_id")\
                else None
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else APIHelper.SKIP
        custom_price =\
            ScheduledRenewalProductPricePoint.from_dictionary(
                dictionary.get("custom_price"))\
                if "custom_price" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(item_id,
                   price_point_id,
                   quantity,
                   custom_price,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.item_type,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.item_id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        int,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("item_type"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("item_id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    int,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _item_type=self.item_type
        _item_id=self.item_id
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _custom_price=(
            self.custom_price
            if hasattr(self, "custom_price")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"item_type={_item_type!r}, "
            f"item_id={_item_id!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"quantity={_quantity!r}, "
            f"custom_price={_custom_price!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _item_type=self.item_type
        _item_id=self.item_id
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _custom_price=(
            self.custom_price
            if hasattr(self, "custom_price")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"item_type={_item_type!s}, "
            f"item_id={_item_id!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"quantity={_quantity!s}, "
            f"custom_price={_custom_price!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
