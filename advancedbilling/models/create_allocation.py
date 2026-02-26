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


class CreateAllocation(object):
    """Implementation of the 'Create Allocation' model.

    Attributes:
        quantity (float): The allocated quantity to which to set the line-items
            allocated quantity. By default, this is an integer. If decimal
            allocations are enabled for the component, it will be a decimal number.
            For On/Off components, use 1for on and 0 for off.
        decimal_quantity (str): Decimal representation of the allocated quantity.
            Only valid when decimal allocations are enabled for the component.
        previous_quantity (float): The quantity that was in effect before this
            allocation. Responses always include this value; it may be supplied on
            preview requests to ensure the expected change is evaluated.
        decimal_previous_quantity (str): Decimal representation of
            `previous_quantity`. Only valid when decimal allocations are enabled for
            the component.
        component_id (int): (required for the multiple allocations endpoint) The id
            associated with the component for which the allocation is being made.
        memo (str): A memo to record along with the allocation.
        proration_downgrade_scheme (str): The scheme used if the proration is a
            downgrade. Defaults to the site setting if one is not provided.
        proration_upgrade_scheme (str): The scheme used if the proration is an
            upgrade. Defaults to the site setting if one is not provided.
        downgrade_credit (DowngradeCreditCreditType): The type of credit to be
            created when upgrading/downgrading. Defaults to the component and then
            site setting if one is not provided. Values are:  `full` -  A full price
            credit is added for the amount owed.   `prorated` - A prorated credit is
            added for the amount owed.   `none` - No charge is added.
        upgrade_charge (UpgradeChargeCreditType): The type of credit to be created
            when upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Values are:  `full` - A charge is added
            for the full price of the component.   `prorated` - A charge is added for
            the prorated price of the component change.  `none` - No charge is added.
        accrue_charge (bool): "If the change in cost is an upgrade, this determines
            if the charge should accrue to the next renewal or if capture should be
            attempted immediately.  `true` - Attempt to charge the customer at the
            next renewal.        `false` - Attempt to charge the customer right away.
            If it fails, the charge will be accrued until the next renewal.  Defaults
            to the site setting if unspecified in the request.
        initiate_dunning (bool): If set to true, if the immediate component payment
            fails, initiate dunning for the subscription.  Otherwise, leave the
            charges on the subscription to pay for at renewal. Defaults to false.
        price_point_id (str | int | None): Price point that the allocation should be
            charged at. Accepts either the price point's id (integer) or handle
            (string). When not specified, the default price point will be used.
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
        "decimal_quantity": "decimal_quantity",
        "previous_quantity": "previous_quantity",
        "decimal_previous_quantity": "decimal_previous_quantity",
        "component_id": "component_id",
        "memo": "memo",
        "proration_downgrade_scheme": "proration_downgrade_scheme",
        "proration_upgrade_scheme": "proration_upgrade_scheme",
        "downgrade_credit": "downgrade_credit",
        "upgrade_charge": "upgrade_charge",
        "accrue_charge": "accrue_charge",
        "initiate_dunning": "initiate_dunning",
        "price_point_id": "price_point_id",
        "billing_schedule": "billing_schedule",
        "custom_price": "custom_price",
    }

    _optionals = [
        "decimal_quantity",
        "previous_quantity",
        "decimal_previous_quantity",
        "component_id",
        "memo",
        "proration_downgrade_scheme",
        "proration_upgrade_scheme",
        "downgrade_credit",
        "upgrade_charge",
        "accrue_charge",
        "initiate_dunning",
        "price_point_id",
        "billing_schedule",
        "custom_price",
    ]

    _nullables = [
        "downgrade_credit",
        "upgrade_charge",
        "price_point_id",
    ]

    def __init__(
        self,
        quantity=None,
        decimal_quantity=APIHelper.SKIP,
        previous_quantity=APIHelper.SKIP,
        decimal_previous_quantity=APIHelper.SKIP,
        component_id=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        proration_downgrade_scheme=APIHelper.SKIP,
        proration_upgrade_scheme=APIHelper.SKIP,
        downgrade_credit=APIHelper.SKIP,
        upgrade_charge=APIHelper.SKIP,
        accrue_charge=APIHelper.SKIP,
        initiate_dunning=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        billing_schedule=APIHelper.SKIP,
        custom_price=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CreateAllocation instance."""
        # Initialize members of the class
        self.quantity = quantity
        if decimal_quantity is not APIHelper.SKIP:
            self.decimal_quantity = decimal_quantity
        if previous_quantity is not APIHelper.SKIP:
            self.previous_quantity = previous_quantity
        if decimal_previous_quantity is not APIHelper.SKIP:
            self.decimal_previous_quantity = decimal_previous_quantity
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if proration_downgrade_scheme is not APIHelper.SKIP:
            self.proration_downgrade_scheme = proration_downgrade_scheme
        if proration_upgrade_scheme is not APIHelper.SKIP:
            self.proration_upgrade_scheme = proration_upgrade_scheme
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge
        if initiate_dunning is not APIHelper.SKIP:
            self.initiate_dunning = initiate_dunning
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else None
        decimal_quantity =\
            dictionary.get("decimal_quantity")\
            if dictionary.get("decimal_quantity")\
                else APIHelper.SKIP
        previous_quantity =\
            dictionary.get("previous_quantity")\
            if dictionary.get("previous_quantity")\
                else APIHelper.SKIP
        decimal_previous_quantity =\
            dictionary.get("decimal_previous_quantity")\
            if dictionary.get("decimal_previous_quantity")\
                else APIHelper.SKIP
        component_id =\
            dictionary.get("component_id")\
            if dictionary.get("component_id")\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP
        proration_downgrade_scheme =\
            dictionary.get("proration_downgrade_scheme")\
            if dictionary.get("proration_downgrade_scheme")\
                else APIHelper.SKIP
        proration_upgrade_scheme =\
            dictionary.get("proration_upgrade_scheme")\
            if dictionary.get("proration_upgrade_scheme")\
                else APIHelper.SKIP
        downgrade_credit =\
            dictionary.get("downgrade_credit")\
            if "downgrade_credit" in dictionary.keys()\
                else APIHelper.SKIP
        upgrade_charge =\
            dictionary.get("upgrade_charge")\
            if "upgrade_charge" in dictionary.keys()\
                else APIHelper.SKIP
        accrue_charge =\
            dictionary.get("accrue_charge")\
            if "accrue_charge" in dictionary.keys()\
                else APIHelper.SKIP
        initiate_dunning =\
            dictionary.get("initiate_dunning")\
            if "initiate_dunning" in dictionary.keys()\
                else APIHelper.SKIP
        if "price_point_id" in dictionary.keys():
            price_point_id = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("CreateAllocationPricePointId"),
            dictionary.get("price_point_id"),
            False)\
            if dictionary.get("price_point_id") is not None\
            else None
        else:
            price_point_id = APIHelper.SKIP
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
                   decimal_quantity,
                   previous_quantity,
                   decimal_previous_quantity,
                   component_id,
                   memo,
                   proration_downgrade_scheme,
                   proration_upgrade_scheme,
                   downgrade_credit,
                   upgrade_charge,
                   accrue_charge,
                   initiate_dunning,
                   price_point_id,
                   billing_schedule,
                   custom_price,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _quantity=self.quantity
        _decimal_quantity=(
            self.decimal_quantity
            if hasattr(self, "decimal_quantity")
            else None
        )
        _previous_quantity=(
            self.previous_quantity
            if hasattr(self, "previous_quantity")
            else None
        )
        _decimal_previous_quantity=(
            self.decimal_previous_quantity
            if hasattr(self, "decimal_previous_quantity")
            else None
        )
        _component_id=(
            self.component_id
            if hasattr(self, "component_id")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _proration_downgrade_scheme=(
            self.proration_downgrade_scheme
            if hasattr(self, "proration_downgrade_scheme")
            else None
        )
        _proration_upgrade_scheme=(
            self.proration_upgrade_scheme
            if hasattr(self, "proration_upgrade_scheme")
            else None
        )
        _downgrade_credit=(
            self.downgrade_credit
            if hasattr(self, "downgrade_credit")
            else None
        )
        _upgrade_charge=(
            self.upgrade_charge
            if hasattr(self, "upgrade_charge")
            else None
        )
        _accrue_charge=(
            self.accrue_charge
            if hasattr(self, "accrue_charge")
            else None
        )
        _initiate_dunning=(
            self.initiate_dunning
            if hasattr(self, "initiate_dunning")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
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
            f"decimal_quantity={_decimal_quantity!r}, "
            f"previous_quantity={_previous_quantity!r}, "
            f"decimal_previous_quantity={_decimal_previous_quantity!r}, "
            f"component_id={_component_id!r}, "
            f"memo={_memo!r}, "
            f"proration_downgrade_scheme={_proration_downgrade_scheme!r}, "
            f"proration_upgrade_scheme={_proration_upgrade_scheme!r}, "
            f"downgrade_credit={_downgrade_credit!r}, "
            f"upgrade_charge={_upgrade_charge!r}, "
            f"accrue_charge={_accrue_charge!r}, "
            f"initiate_dunning={_initiate_dunning!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"billing_schedule={_billing_schedule!r}, "
            f"custom_price={_custom_price!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _quantity=self.quantity
        _decimal_quantity=(
            self.decimal_quantity
            if hasattr(self, "decimal_quantity")
            else None
        )
        _previous_quantity=(
            self.previous_quantity
            if hasattr(self, "previous_quantity")
            else None
        )
        _decimal_previous_quantity=(
            self.decimal_previous_quantity
            if hasattr(self, "decimal_previous_quantity")
            else None
        )
        _component_id=(
            self.component_id
            if hasattr(self, "component_id")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _proration_downgrade_scheme=(
            self.proration_downgrade_scheme
            if hasattr(self, "proration_downgrade_scheme")
            else None
        )
        _proration_upgrade_scheme=(
            self.proration_upgrade_scheme
            if hasattr(self, "proration_upgrade_scheme")
            else None
        )
        _downgrade_credit=(
            self.downgrade_credit
            if hasattr(self, "downgrade_credit")
            else None
        )
        _upgrade_charge=(
            self.upgrade_charge
            if hasattr(self, "upgrade_charge")
            else None
        )
        _accrue_charge=(
            self.accrue_charge
            if hasattr(self, "accrue_charge")
            else None
        )
        _initiate_dunning=(
            self.initiate_dunning
            if hasattr(self, "initiate_dunning")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
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
            f"decimal_quantity={_decimal_quantity!s}, "
            f"previous_quantity={_previous_quantity!s}, "
            f"decimal_previous_quantity={_decimal_previous_quantity!s}, "
            f"component_id={_component_id!s}, "
            f"memo={_memo!s}, "
            f"proration_downgrade_scheme={_proration_downgrade_scheme!s}, "
            f"proration_upgrade_scheme={_proration_upgrade_scheme!s}, "
            f"downgrade_credit={_downgrade_credit!s}, "
            f"upgrade_charge={_upgrade_charge!s}, "
            f"accrue_charge={_accrue_charge!s}, "
            f"initiate_dunning={_initiate_dunning!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"billing_schedule={_billing_schedule!s}, "
            f"custom_price={_custom_price!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
