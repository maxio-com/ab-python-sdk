# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AllocationPreviewItem(object):

    """Implementation of the 'Allocation Preview Item' model.

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        subscription_id (int): TODO: type description here.
        quantity (int | str | None): TODO: type description here.
        previous_quantity (int | str | None): TODO: type description here.
        memo (str): TODO: type description here.
        timestamp (str): TODO: type description here.
        proration_upgrade_scheme (str): TODO: type description here.
        proration_downgrade_scheme (str): TODO: type description here.
        accrue_charge (bool): TODO: type description here.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        price_point_id (int): TODO: type description here.
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        previous_price_point_id (int): TODO: type description here.
        price_point_handle (str): TODO: type description here.
        price_point_name (str): TODO: type description here.
        component_handle (str): TODO: type description here.

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
                 component_handle=APIHelper.SKIP):
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
        if dictionary is None:
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
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        previous_price_point_id = dictionary.get("previous_price_point_id") if dictionary.get("previous_price_point_id") else APIHelper.SKIP
        price_point_handle = dictionary.get("price_point_handle") if dictionary.get("price_point_handle") else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if dictionary.get("price_point_name") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if "component_handle" in dictionary.keys() else APIHelper.SKIP
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
                   component_handle)
