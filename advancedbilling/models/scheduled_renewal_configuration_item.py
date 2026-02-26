"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ScheduledRenewalConfigurationItem(object):
    """Implementation of the 'Scheduled Renewal Configuration Item' model.

    Attributes:
        id (int): The model property of type int.
        subscription_id (int): The model property of type int.
        subscription_renewal_configuration_id (int): The model property of type int.
        item_id (int): The model property of type int.
        item_type (str): The model property of type str.
        item_subclass (str): The model property of type str.
        price_point_id (int): The model property of type int.
        price_point_type (str): The model property of type str.
        quantity (int): The model property of type int.
        decimal_quantity (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "subscription_id": "subscription_id",
        "subscription_renewal_configuration_id":
            "subscription_renewal_configuration_id",
        "item_id": "item_id",
        "item_type": "item_type",
        "item_subclass": "item_subclass",
        "price_point_id": "price_point_id",
        "price_point_type": "price_point_type",
        "quantity": "quantity",
        "decimal_quantity": "decimal_quantity",
        "created_at": "created_at",
    }

    _optionals = [
        "id",
        "subscription_id",
        "subscription_renewal_configuration_id",
        "item_id",
        "item_type",
        "item_subclass",
        "price_point_id",
        "price_point_type",
        "quantity",
        "decimal_quantity",
        "created_at",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        subscription_id=APIHelper.SKIP,
        subscription_renewal_configuration_id=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        item_type=APIHelper.SKIP,
        item_subclass=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        price_point_type=APIHelper.SKIP,
        quantity=APIHelper.SKIP,
        decimal_quantity=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalConfigurationItem instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id
        if subscription_renewal_configuration_id is not APIHelper.SKIP:
            self.subscription_renewal_configuration_id =\
                 subscription_renewal_configuration_id
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if item_type is not APIHelper.SKIP:
            self.item_type = item_type
        if item_subclass is not APIHelper.SKIP:
            self.item_subclass = item_subclass
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if price_point_type is not APIHelper.SKIP:
            self.price_point_type = price_point_type
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity
        if decimal_quantity is not APIHelper.SKIP:
            self.decimal_quantity = decimal_quantity
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        subscription_id =\
            dictionary.get("subscription_id")\
            if dictionary.get("subscription_id")\
                else APIHelper.SKIP
        subscription_renewal_configuration_id =\
            dictionary.get("subscription_renewal_configuration_id")\
            if dictionary.get("subscription_renewal_configuration_id")\
                else APIHelper.SKIP
        item_id =\
            dictionary.get("item_id")\
            if dictionary.get("item_id")\
                else APIHelper.SKIP
        item_type =\
            dictionary.get("item_type")\
            if dictionary.get("item_type")\
                else APIHelper.SKIP
        item_subclass =\
            dictionary.get("item_subclass")\
            if dictionary.get("item_subclass")\
                else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP
        price_point_type =\
            dictionary.get("price_point_type")\
            if dictionary.get("price_point_type")\
                else APIHelper.SKIP
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else APIHelper.SKIP
        decimal_quantity =\
            dictionary.get("decimal_quantity")\
            if dictionary.get("decimal_quantity")\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   subscription_id,
                   subscription_renewal_configuration_id,
                   item_id,
                   item_type,
                   item_subclass,
                   price_point_id,
                   price_point_type,
                   quantity,
                   decimal_quantity,
                   created_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _subscription_renewal_configuration_id=(
            self.subscription_renewal_configuration_id
            if hasattr(self, "subscription_renewal_configuration_id")
            else None
        )
        _item_id=(
            self.item_id
            if hasattr(self, "item_id")
            else None
        )
        _item_type=(
            self.item_type
            if hasattr(self, "item_type")
            else None
        )
        _item_subclass=(
            self.item_subclass
            if hasattr(self, "item_subclass")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _price_point_type=(
            self.price_point_type
            if hasattr(self, "price_point_type")
            else None
        )
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _decimal_quantity=(
            self.decimal_quantity
            if hasattr(self, "decimal_quantity")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"subscription_id={_subscription_id!r}, "
            f"subscription_renewal_configuration_id={_subscription_renewal_configuration_id!r}, "
            f"item_id={_item_id!r}, "
            f"item_type={_item_type!r}, "
            f"item_subclass={_item_subclass!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"price_point_type={_price_point_type!r}, "
            f"quantity={_quantity!r}, "
            f"decimal_quantity={_decimal_quantity!r}, "
            f"created_at={_created_at!r}, "
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
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _subscription_renewal_configuration_id=(
            self.subscription_renewal_configuration_id
            if hasattr(self, "subscription_renewal_configuration_id")
            else None
        )
        _item_id=(
            self.item_id
            if hasattr(self, "item_id")
            else None
        )
        _item_type=(
            self.item_type
            if hasattr(self, "item_type")
            else None
        )
        _item_subclass=(
            self.item_subclass
            if hasattr(self, "item_subclass")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _price_point_type=(
            self.price_point_type
            if hasattr(self, "price_point_type")
            else None
        )
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _decimal_quantity=(
            self.decimal_quantity
            if hasattr(self, "decimal_quantity")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"subscription_id={_subscription_id!s}, "
            f"subscription_renewal_configuration_id={_subscription_renewal_configuration_id!s}, "
            f"item_id={_item_id!s}, "
            f"item_type={_item_type!s}, "
            f"item_subclass={_item_subclass!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"price_point_type={_price_point_type!s}, "
            f"quantity={_quantity!s}, "
            f"decimal_quantity={_decimal_quantity!s}, "
            f"created_at={_created_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
