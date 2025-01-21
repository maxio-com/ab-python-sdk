# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_schedule import BillingSchedule


class CreateAllocation(object):

    """Implementation of the 'Create Allocation' model.

    Attributes:
        quantity (float): The allocated quantity to which to set the
            line-items allocated quantity. By default, this is an integer. If
            decimal allocations are enabled for the component, it will be a
            decimal number. For On/Off components, use 1for on and 0 for off.
        component_id (int): (required for the multiple allocations endpoint)
            The id associated with the component for which the allocation is
            being made
        memo (str): A memo to record along with the allocation
        proration_downgrade_scheme (str): The scheme used if the proration is
            a downgrade. Defaults to the site setting if one is not provided.
        proration_upgrade_scheme (str): The scheme used if the proration is an
            upgrade. Defaults to the site setting if one is not provided.
        accrue_charge (bool): If the change in cost is an upgrade, this
            determines if the charge should accrue to the next renewal or if
            capture should be attempted immediately. Defaults to the site
            setting if one is not provided.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        initiate_dunning (bool): If set to true, if the immediate component
            payment fails, initiate dunning for the subscription.  Otherwise,
            leave the charges on the subscription to pay for at renewal.
            Defaults to false.
        price_point_id (str | int | None): Price point that the allocation
            should be charged at. Accepts either the price point's id
            (integer) or handle (string). When not specified, the default
            price point will be used.
        billing_schedule (BillingSchedule): This attribute is particularly
            useful when you need to align billing events for different
            components on distinct schedules within a subscription. Please
            note this only works for site with Multifrequency enabled
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": 'quantity',
        "component_id": 'component_id',
        "memo": 'memo',
        "proration_downgrade_scheme": 'proration_downgrade_scheme',
        "proration_upgrade_scheme": 'proration_upgrade_scheme',
        "accrue_charge": 'accrue_charge',
        "downgrade_credit": 'downgrade_credit',
        "upgrade_charge": 'upgrade_charge',
        "initiate_dunning": 'initiate_dunning',
        "price_point_id": 'price_point_id',
        "billing_schedule": 'billing_schedule'
    }

    _optionals = [
        'component_id',
        'memo',
        'proration_downgrade_scheme',
        'proration_upgrade_scheme',
        'accrue_charge',
        'downgrade_credit',
        'upgrade_charge',
        'initiate_dunning',
        'price_point_id',
        'billing_schedule',
    ]

    _nullables = [
        'downgrade_credit',
        'upgrade_charge',
        'price_point_id',
    ]

    def __init__(self,
                 quantity=None,
                 component_id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 proration_downgrade_scheme=APIHelper.SKIP,
                 proration_upgrade_scheme=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 initiate_dunning=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 billing_schedule=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateAllocation class"""

        # Initialize members of the class
        self.quantity = quantity 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if proration_downgrade_scheme is not APIHelper.SKIP:
            self.proration_downgrade_scheme = proration_downgrade_scheme 
        if proration_upgrade_scheme is not APIHelper.SKIP:
            self.proration_upgrade_scheme = proration_upgrade_scheme 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if initiate_dunning is not APIHelper.SKIP:
            self.initiate_dunning = initiate_dunning 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if billing_schedule is not APIHelper.SKIP:
            self.billing_schedule = billing_schedule 

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
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else APIHelper.SKIP
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        initiate_dunning = dictionary.get("initiate_dunning") if "initiate_dunning" in dictionary.keys() else APIHelper.SKIP
        if 'price_point_id' in dictionary.keys():
            price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateAllocationPricePointId'), dictionary.get('price_point_id'), False) if dictionary.get('price_point_id') is not None else None
        else:
            price_point_id = APIHelper.SKIP
        billing_schedule = BillingSchedule.from_dictionary(dictionary.get('billing_schedule')) if 'billing_schedule' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(quantity,
                   component_id,
                   memo,
                   proration_downgrade_scheme,
                   proration_upgrade_scheme,
                   accrue_charge,
                   downgrade_credit,
                   upgrade_charge,
                   initiate_dunning,
                   price_point_id,
                   billing_schedule,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'quantity={self.quantity!r}, '
                f'component_id={self.component_id!r}, '
                f'memo={self.memo!r}, '
                f'proration_downgrade_scheme={self.proration_downgrade_scheme!r}, '
                f'proration_upgrade_scheme={self.proration_upgrade_scheme!r}, '
                f'accrue_charge={self.accrue_charge!r}, '
                f'downgrade_credit={self.downgrade_credit!r}, '
                f'upgrade_charge={self.upgrade_charge!r}, '
                f'initiate_dunning={self.initiate_dunning!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'billing_schedule={self.billing_schedule!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'quantity={self.quantity!s}, '
                f'component_id={self.component_id!s}, '
                f'memo={self.memo!s}, '
                f'proration_downgrade_scheme={self.proration_downgrade_scheme!s}, '
                f'proration_upgrade_scheme={self.proration_upgrade_scheme!s}, '
                f'accrue_charge={self.accrue_charge!s}, '
                f'downgrade_credit={self.downgrade_credit!s}, '
                f'upgrade_charge={self.upgrade_charge!s}, '
                f'initiate_dunning={self.initiate_dunning!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'billing_schedule={self.billing_schedule!s}, '
                f'additional_properties={self.additional_properties!s})')
