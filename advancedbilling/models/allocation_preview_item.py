# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AllocationPreviewItem(object):

    """Implementation of the 'Allocation Preview Item' model.

    Attributes:
        component_id (int): The model property of type int.
        subscription_id (int): The model property of type int.
        quantity (int | str | None): The model property of type int | str |
            None.
        previous_quantity (int | str | None): The model property of type int |
            str | None.
        memo (str): The model property of type str.
        timestamp (str): The model property of type str.
        proration_upgrade_scheme (str): The model property of type str.
        proration_downgrade_scheme (str): The model property of type str.
        accrue_charge (bool): The model property of type bool.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        price_point_id (int): The model property of type int.
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        previous_price_point_id (int): The model property of type int.
        price_point_handle (str): The model property of type str.
        price_point_name (str): The model property of type str.
        component_handle (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "subscription_id": 'subscription_id',
        "quantity": 'quantity',
        "previous_quantity": 'previous_quantity',
        "memo": 'memo',
        "timestamp": 'timestamp',
        "proration_upgrade_scheme": 'proration_upgrade_scheme',
        "proration_downgrade_scheme": 'proration_downgrade_scheme',
        "accrue_charge": 'accrue_charge',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "price_point_id": 'price_point_id',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "previous_price_point_id": 'previous_price_point_id',
        "price_point_handle": 'price_point_handle',
        "price_point_name": 'price_point_name',
        "component_handle": 'component_handle'
    }

    _optionals = [
        'component_id',
        'subscription_id',
        'quantity',
        'previous_quantity',
        'memo',
        'timestamp',
        'proration_upgrade_scheme',
        'proration_downgrade_scheme',
        'accrue_charge',
        'upgrade_charge',
        'downgrade_credit',
        'price_point_id',
        'interval',
        'interval_unit',
        'previous_price_point_id',
        'price_point_handle',
        'price_point_name',
        'component_handle',
    ]

    _nullables = [
        'memo',
        'timestamp',
        'upgrade_charge',
        'downgrade_credit',
        'interval_unit',
        'component_handle',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 previous_quantity=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP,
                 proration_upgrade_scheme=APIHelper.SKIP,
                 proration_downgrade_scheme=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 previous_price_point_id=APIHelper.SKIP,
                 price_point_handle=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AllocationPreviewItem class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if previous_quantity is not APIHelper.SKIP:
            self.previous_quantity = previous_quantity 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 
        if proration_upgrade_scheme is not APIHelper.SKIP:
            self.proration_upgrade_scheme = proration_upgrade_scheme 
        if proration_downgrade_scheme is not APIHelper.SKIP:
            self.proration_downgrade_scheme = proration_downgrade_scheme 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if previous_price_point_id is not APIHelper.SKIP:
            self.previous_price_point_id = previous_price_point_id 
        if price_point_handle is not APIHelper.SKIP:
            self.price_point_handle = price_point_handle 
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('AllocationPreviewItemQuantity'), dictionary.get('quantity'), False) if dictionary.get('quantity') is not None else APIHelper.SKIP
        previous_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('AllocationPreviewItemPreviousQuantity'), dictionary.get('previous_quantity'), False) if dictionary.get('previous_quantity') is not None else APIHelper.SKIP
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        timestamp = dictionary.get("timestamp") if "timestamp" in dictionary.keys() else APIHelper.SKIP
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else APIHelper.SKIP
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        previous_price_point_id = dictionary.get("previous_price_point_id") if dictionary.get("previous_price_point_id") else APIHelper.SKIP
        price_point_handle = dictionary.get("price_point_handle") if dictionary.get("price_point_handle") else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if dictionary.get("price_point_name") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if "component_handle" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   subscription_id,
                   quantity,
                   previous_quantity,
                   memo,
                   timestamp,
                   proration_upgrade_scheme,
                   proration_downgrade_scheme,
                   accrue_charge,
                   upgrade_charge,
                   downgrade_credit,
                   price_point_id,
                   interval,
                   interval_unit,
                   previous_price_point_id,
                   price_point_handle,
                   price_point_name,
                   component_handle,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'previous_quantity={(self.previous_quantity if hasattr(self, "previous_quantity") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'timestamp={(self.timestamp if hasattr(self, "timestamp") else None)!r}, '
                f'proration_upgrade_scheme={(self.proration_upgrade_scheme if hasattr(self, "proration_upgrade_scheme") else None)!r}, '
                f'proration_downgrade_scheme={(self.proration_downgrade_scheme if hasattr(self, "proration_downgrade_scheme") else None)!r}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!r}, '
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!r}, '
                f'downgrade_credit={(self.downgrade_credit if hasattr(self, "downgrade_credit") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!r}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!r}, '
                f'previous_price_point_id={(self.previous_price_point_id if hasattr(self, "previous_price_point_id") else None)!r}, '
                f'price_point_handle={(self.price_point_handle if hasattr(self, "price_point_handle") else None)!r}, '
                f'price_point_name={(self.price_point_name if hasattr(self, "price_point_name") else None)!r}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'previous_quantity={(self.previous_quantity if hasattr(self, "previous_quantity") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'timestamp={(self.timestamp if hasattr(self, "timestamp") else None)!s}, '
                f'proration_upgrade_scheme={(self.proration_upgrade_scheme if hasattr(self, "proration_upgrade_scheme") else None)!s}, '
                f'proration_downgrade_scheme={(self.proration_downgrade_scheme if hasattr(self, "proration_downgrade_scheme") else None)!s}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!s}, '
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!s}, '
                f'downgrade_credit={(self.downgrade_credit if hasattr(self, "downgrade_credit") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!s}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!s}, '
                f'previous_price_point_id={(self.previous_price_point_id if hasattr(self, "previous_price_point_id") else None)!s}, '
                f'price_point_handle={(self.price_point_handle if hasattr(self, "price_point_handle") else None)!s}, '
                f'price_point_name={(self.price_point_name if hasattr(self, "price_point_name") else None)!s}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
