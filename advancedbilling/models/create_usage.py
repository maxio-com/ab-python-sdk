"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_schedule import (
    BillingSchedule,
)
from advancedbilling.models.component_custom_price import (
    ComponentCustomPrice,
)


class CreateUsage(object):
    """Implementation of the 'Create Usage' model.

    Attributes:
        quantity (float): integer by default or decimal number if fractional
            quantities are enabled for the component
        price_point_id (str): The model property of type str.
        memo (str): The model property of type str.
        billing_schedule (BillingSchedule): This attribute is particularly useful
            when you need to align billing events for different components on
            distinct schedules within a subscription. This only works for site with
            Multifrequency enabled.
        custom_price (ComponentCustomPrice): Create or update custom pricing unique
            to the subscription. Used in place of `price_point_id`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": "quantity",
        "price_point_id": "price_point_id",
        "memo": "memo",
        "billing_schedule": "billing_schedule",
        "custom_price": "custom_price",
    }

    _optionals = [
        "quantity",
        "price_point_id",
        "memo",
        "billing_schedule",
        "custom_price",
    ]

    def __init__(
        self,
        quantity=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        billing_schedule=APIHelper.SKIP,
        custom_price=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CreateUsage instance."""
        # Initialize members of the class
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if billing_schedule is not APIHelper.SKIP:
            self.billing_schedule = billing_schedule
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
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP
        billing_schedule =\
            BillingSchedule.from_dictionary(
                dictionary.get("billing_schedule"))\
                if "billing_schedule" in dictionary.keys()\
                else APIHelper.SKIP
        custom_price =\
            ComponentCustomPrice.from_dictionary(
                dictionary.get("custom_price"))\
                if "custom_price" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(quantity,
                   price_point_id,
                   memo,
                   billing_schedule,
                   custom_price,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _billing_schedule=(
            self.billing_schedule
            if hasattr(self, "billing_schedule")
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
            f"quantity={_quantity!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"memo={_memo!r}, "
            f"billing_schedule={_billing_schedule!r}, "
            f"custom_price={_custom_price!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _billing_schedule=(
            self.billing_schedule
            if hasattr(self, "billing_schedule")
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
            f"quantity={_quantity!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"memo={_memo!s}, "
            f"billing_schedule={_billing_schedule!s}, "
            f"custom_price={_custom_price!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
