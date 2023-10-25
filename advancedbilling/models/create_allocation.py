# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateAllocation(object):

    """Implementation of the 'Create Allocation' model.

    TODO: type model description here.

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
        downgrade_credit (CreditType1): The type of credit to be created if
            the change in cost is a downgrade. Defaults to the component and
            then site setting if one is not provided.
        upgrade_charge (CreditType1): The type of charge to be created if the
            change in cost is an upgrade. Defaults to the component and then
            site setting if one is not provided.
        price_point_id (str | int | None): Price point that the allocation
            should be charged at. Accepts either the price point's id
            (integer) or handle (string). When not specified, the default
            price point will be used.

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
        "price_point_id": 'price_point_id'
    }

    _optionals = [
        'component_id',
        'memo',
        'proration_downgrade_scheme',
        'proration_upgrade_scheme',
        'accrue_charge',
        'downgrade_credit',
        'upgrade_charge',
        'price_point_id',
    ]

    _nullables = [
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
                 price_point_id=APIHelper.SKIP):
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
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else APIHelper.SKIP
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if dictionary.get("downgrade_credit") else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if dictionary.get("upgrade_charge") else APIHelper.SKIP
        if 'price_point_id' in dictionary.keys():
            price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateAllocationPricePointId'), dictionary.get('price_point_id'), False) if dictionary.get('price_point_id') is not None else None
        else:
            price_point_id = APIHelper.SKIP
        # Return an object of this model
        return cls(quantity,
                   component_id,
                   memo,
                   proration_downgrade_scheme,
                   proration_upgrade_scheme,
                   accrue_charge,
                   downgrade_credit,
                   upgrade_charge,
                   price_point_id)
