# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payment_for_allocation import PaymentForAllocation


class Allocation(object):

    """Implementation of the 'Allocation' model.

    Attributes:
        allocation_id (int): The allocation unique id
        component_id (int): The integer component ID for the allocation. This
            references a component that you have created in your Product setup
        component_handle (str): The handle of the component. This references a
            component that you have created in your Product setup
        subscription_id (int): The integer subscription ID for the allocation.
            This references a unique subscription in your Site
        quantity (int | str | None): The allocated quantity set in to effect
            by the allocation. String for components supporting fractional
            quantities
        previous_quantity (int | str | None): The allocated quantity that was
            in effect before this allocation was created. String for
            components supporting fractional quantities
        memo (str): The memo passed when the allocation was created
        timestamp (datetime): The time that the allocation was recorded, in
            format and UTC timezone, i.e. 2012-11-20T22:00:37Z
        created_at (datetime): Timestamp indicating when this allocation was
            created
        proration_upgrade_scheme (str): The scheme used if the proration was
            an upgrade. This is only present when the allocation was created
            mid-period.
        proration_downgrade_scheme (str): The scheme used if the proration was
            a downgrade. This is only present when the allocation was created
            mid-period.
        price_point_id (int): The model property of type int.
        price_point_name (str): The model property of type str.
        price_point_handle (str): The model property of type str.
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        previous_price_point_id (int): The model property of type int.
        accrue_charge (bool): If the change in cost is an upgrade, this
            determines if the charge should accrue to the next renewal or if
            capture should be attempted immediately.
        initiate_dunning (bool): If true, if the immediate component payment
            fails, initiate dunning for the subscription.  Otherwise, leave
            the charges on the subscription to pay for at renewal.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        payment (PaymentForAllocation): The model property of type
            PaymentForAllocation.
        expires_at (datetime): The model property of type datetime.
        used_quantity (int): The model property of type int.
        charge_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocation_id": 'allocation_id',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "subscription_id": 'subscription_id',
        "quantity": 'quantity',
        "previous_quantity": 'previous_quantity',
        "memo": 'memo',
        "timestamp": 'timestamp',
        "created_at": 'created_at',
        "proration_upgrade_scheme": 'proration_upgrade_scheme',
        "proration_downgrade_scheme": 'proration_downgrade_scheme',
        "price_point_id": 'price_point_id',
        "price_point_name": 'price_point_name',
        "price_point_handle": 'price_point_handle',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "previous_price_point_id": 'previous_price_point_id',
        "accrue_charge": 'accrue_charge',
        "initiate_dunning": 'initiate_dunning',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "payment": 'payment',
        "expires_at": 'expires_at',
        "used_quantity": 'used_quantity',
        "charge_id": 'charge_id'
    }

    _optionals = [
        'allocation_id',
        'component_id',
        'component_handle',
        'subscription_id',
        'quantity',
        'previous_quantity',
        'memo',
        'timestamp',
        'created_at',
        'proration_upgrade_scheme',
        'proration_downgrade_scheme',
        'price_point_id',
        'price_point_name',
        'price_point_handle',
        'interval',
        'interval_unit',
        'previous_price_point_id',
        'accrue_charge',
        'initiate_dunning',
        'upgrade_charge',
        'downgrade_credit',
        'payment',
        'expires_at',
        'used_quantity',
        'charge_id',
    ]

    _nullables = [
        'component_handle',
        'memo',
        'interval_unit',
        'upgrade_charge',
        'downgrade_credit',
        'payment',
    ]

    def __init__(self,
                 allocation_id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 previous_quantity=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 proration_upgrade_scheme=APIHelper.SKIP,
                 proration_downgrade_scheme=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 price_point_handle=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 previous_price_point_id=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 initiate_dunning=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 payment=APIHelper.SKIP,
                 expires_at=APIHelper.SKIP,
                 used_quantity=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Allocation class"""

        # Initialize members of the class
        if allocation_id is not APIHelper.SKIP:
            self.allocation_id = allocation_id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if previous_quantity is not APIHelper.SKIP:
            self.previous_quantity = previous_quantity 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = APIHelper.apply_datetime_converter(timestamp, APIHelper.RFC3339DateTime) if timestamp else None 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if proration_upgrade_scheme is not APIHelper.SKIP:
            self.proration_upgrade_scheme = proration_upgrade_scheme 
        if proration_downgrade_scheme is not APIHelper.SKIP:
            self.proration_downgrade_scheme = proration_downgrade_scheme 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name 
        if price_point_handle is not APIHelper.SKIP:
            self.price_point_handle = price_point_handle 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if previous_price_point_id is not APIHelper.SKIP:
            self.previous_price_point_id = previous_price_point_id 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 
        if initiate_dunning is not APIHelper.SKIP:
            self.initiate_dunning = initiate_dunning 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
        if used_quantity is not APIHelper.SKIP:
            self.used_quantity = used_quantity 
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        allocation_id = dictionary.get("allocation_id") if dictionary.get("allocation_id") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if "component_handle" in dictionary.keys() else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('AllocationQuantity'), dictionary.get('quantity'), False) if dictionary.get('quantity') is not None else APIHelper.SKIP
        previous_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('AllocationPreviousQuantity'), dictionary.get('previous_quantity'), False) if dictionary.get('previous_quantity') is not None else APIHelper.SKIP
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else APIHelper.SKIP
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if dictionary.get("price_point_name") else APIHelper.SKIP
        price_point_handle = dictionary.get("price_point_handle") if dictionary.get("price_point_handle") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        previous_price_point_id = dictionary.get("previous_price_point_id") if dictionary.get("previous_price_point_id") else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        initiate_dunning = dictionary.get("initiate_dunning") if "initiate_dunning" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        if 'payment' in dictionary.keys():
            payment = PaymentForAllocation.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        else:
            payment = APIHelper.SKIP
        expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else APIHelper.SKIP
        used_quantity = dictionary.get("used_quantity") if dictionary.get("used_quantity") else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if dictionary.get("charge_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(allocation_id,
                   component_id,
                   component_handle,
                   subscription_id,
                   quantity,
                   previous_quantity,
                   memo,
                   timestamp,
                   created_at,
                   proration_upgrade_scheme,
                   proration_downgrade_scheme,
                   price_point_id,
                   price_point_name,
                   price_point_handle,
                   interval,
                   interval_unit,
                   previous_price_point_id,
                   accrue_charge,
                   initiate_dunning,
                   upgrade_charge,
                   downgrade_credit,
                   payment,
                   expires_at,
                   used_quantity,
                   charge_id,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'allocation_id={(self.allocation_id if hasattr(self, "allocation_id") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'previous_quantity={(self.previous_quantity if hasattr(self, "previous_quantity") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'timestamp={(self.timestamp if hasattr(self, "timestamp") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'proration_upgrade_scheme={(self.proration_upgrade_scheme if hasattr(self, "proration_upgrade_scheme") else None)!r}, '
                f'proration_downgrade_scheme={(self.proration_downgrade_scheme if hasattr(self, "proration_downgrade_scheme") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'price_point_name={(self.price_point_name if hasattr(self, "price_point_name") else None)!r}, '
                f'price_point_handle={(self.price_point_handle if hasattr(self, "price_point_handle") else None)!r}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!r}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!r}, '
                f'previous_price_point_id={(self.previous_price_point_id if hasattr(self, "previous_price_point_id") else None)!r}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!r}, '
                f'initiate_dunning={(self.initiate_dunning if hasattr(self, "initiate_dunning") else None)!r}, '
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!r}, '
                f'downgrade_credit={(self.downgrade_credit if hasattr(self, "downgrade_credit") else None)!r}, '
                f'payment={(self.payment if hasattr(self, "payment") else None)!r}, '
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!r}, '
                f'used_quantity={(self.used_quantity if hasattr(self, "used_quantity") else None)!r}, '
                f'charge_id={(self.charge_id if hasattr(self, "charge_id") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'allocation_id={(self.allocation_id if hasattr(self, "allocation_id") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'previous_quantity={(self.previous_quantity if hasattr(self, "previous_quantity") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'timestamp={(self.timestamp if hasattr(self, "timestamp") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'proration_upgrade_scheme={(self.proration_upgrade_scheme if hasattr(self, "proration_upgrade_scheme") else None)!s}, '
                f'proration_downgrade_scheme={(self.proration_downgrade_scheme if hasattr(self, "proration_downgrade_scheme") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'price_point_name={(self.price_point_name if hasattr(self, "price_point_name") else None)!s}, '
                f'price_point_handle={(self.price_point_handle if hasattr(self, "price_point_handle") else None)!s}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!s}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!s}, '
                f'previous_price_point_id={(self.previous_price_point_id if hasattr(self, "previous_price_point_id") else None)!s}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!s}, '
                f'initiate_dunning={(self.initiate_dunning if hasattr(self, "initiate_dunning") else None)!s}, '
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!s}, '
                f'downgrade_credit={(self.downgrade_credit if hasattr(self, "downgrade_credit") else None)!s}, '
                f'payment={(self.payment if hasattr(self, "payment") else None)!s}, '
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!s}, '
                f'used_quantity={(self.used_quantity if hasattr(self, "used_quantity") else None)!s}, '
                f'charge_id={(self.charge_id if hasattr(self, "charge_id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
