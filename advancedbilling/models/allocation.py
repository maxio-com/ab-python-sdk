# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Allocation(object):

    """Implementation of the 'Allocation' model.

    TODO: type model description here.

    Attributes:
        component_id (int): The integer component ID for the allocation. This
            references a component that you have created in your Product
            setup
        subscription_id (int): The integer subscription ID for the allocation.
            This references a unique subscription in your Site
        quantity (int): The allocated quantity set in to effect by the
            allocation
        previous_quantity (int): The allocated quantity that was in effect
            before this allocation was created
        memo (str): The memo passed when the allocation was created
        timestamp (str): The time that the allocation was recorded, in  format
            and UTC timezone, i.e. 2012-11-20T22:00:37Z
        proration_upgrade_scheme (str): The scheme used if the proration was
            an upgrade. This is only present when the allocation was created
            mid-period.
        proration_downgrade_scheme (str): The scheme used if the proration was
            a downgrade. This is only present when the allocation was created
            mid-period.
        price_point_id (int): TODO: type description here.
        price_point_name (str): TODO: type description here.
        price_point_handle (str): TODO: type description here.
        previous_price_point_id (int): TODO: type description here.
        accrue_charge (bool): If the change in cost is an upgrade, this
            determines if the charge should accrue to the next renewal or if
            capture should be attempted immediately.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        payment (AllocationPayment | None): TODO: type description here.

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
        "price_point_id": 'price_point_id',
        "price_point_name": 'price_point_name',
        "price_point_handle": 'price_point_handle',
        "previous_price_point_id": 'previous_price_point_id',
        "accrue_charge": 'accrue_charge',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "payment": 'payment'
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
        'price_point_id',
        'price_point_name',
        'price_point_handle',
        'previous_price_point_id',
        'accrue_charge',
        'upgrade_charge',
        'downgrade_credit',
        'payment',
    ]

    _nullables = [
        'memo',
        'upgrade_charge',
        'downgrade_credit',
        'payment',
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
                 price_point_id=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 price_point_handle=APIHelper.SKIP,
                 previous_price_point_id=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 payment=APIHelper.SKIP):
        """Constructor for the Allocation class"""

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
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name 
        if price_point_handle is not APIHelper.SKIP:
            self.price_point_handle = price_point_handle 
        if previous_price_point_id is not APIHelper.SKIP:
            self.previous_price_point_id = previous_price_point_id 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if payment is not APIHelper.SKIP:
            self.payment = payment 

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
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        previous_quantity = dictionary.get("previous_quantity") if dictionary.get("previous_quantity") else APIHelper.SKIP
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else APIHelper.SKIP
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else APIHelper.SKIP
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if dictionary.get("price_point_name") else APIHelper.SKIP
        price_point_handle = dictionary.get("price_point_handle") if dictionary.get("price_point_handle") else APIHelper.SKIP
        previous_price_point_id = dictionary.get("previous_price_point_id") if dictionary.get("previous_price_point_id") else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        if 'payment' in dictionary.keys():
            payment = APIHelper.deserialize_union_type(UnionTypeLookUp.get('AllocationPayment2'), dictionary.get('payment'), False) if dictionary.get('payment') is not None else None
        else:
            payment = APIHelper.SKIP
        # Return an object of this model
        return cls(component_id,
                   subscription_id,
                   quantity,
                   previous_quantity,
                   memo,
                   timestamp,
                   proration_upgrade_scheme,
                   proration_downgrade_scheme,
                   price_point_id,
                   price_point_name,
                   price_point_handle,
                   previous_price_point_id,
                   accrue_charge,
                   upgrade_charge,
                   downgrade_credit,
                   payment)
