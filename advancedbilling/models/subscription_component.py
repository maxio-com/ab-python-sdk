# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_component_subscription import SubscriptionComponentSubscription


class SubscriptionComponent(object):

    """Implementation of the 'Subscription Component' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (str): TODO: type description here.
        kind (str): TODO: type description here.
        unit_name (str): TODO: type description here.
        enabled (bool): (for on/off components) indicates if the component is
            enabled for the subscription
        unit_balance (int): TODO: type description here.
        currency (str): TODO: type description here.
        allocated_quantity (int): For Quantity-based components: The current
            allocation for the component on the given subscription. For On/Off
            components: Use 1 for on. Use 0 for off.
        pricing_scheme (str): TODO: type description here.
        component_id (int): TODO: type description here.
        component_handle (str): TODO: type description here.
        subscription_id (int): TODO: type description here.
        recurring (bool): TODO: type description here.
        upgrade_charge (str): TODO: type description here.
        downgrade_credit (str): TODO: type description here.
        archived_at (str): TODO: type description here.
        price_point_id (int): TODO: type description here.
        price_point_handle (str): TODO: type description here.
        price_point_type (PricePointTypeOneOf0 | PricePointType | None): TODO:
            type description here.
        price_point_name (str): TODO: type description here.
        product_family_id (int): TODO: type description here.
        product_family_handle (str): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
        use_site_exchange_rate (bool): TODO: type description here.
        description (str): TODO: type description here.
        allow_fractional_quantities (bool): TODO: type description here.
        subscription (SubscriptionComponentSubscription): An optional object,
            will be returned if provided `include=subscription` query param.
        display_on_hosted_page (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "kind": 'kind',
        "unit_name": 'unit_name',
        "enabled": 'enabled',
        "unit_balance": 'unit_balance',
        "currency": 'currency',
        "allocated_quantity": 'allocated_quantity',
        "pricing_scheme": 'pricing_scheme',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "subscription_id": 'subscription_id',
        "recurring": 'recurring',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "archived_at": 'archived_at',
        "price_point_id": 'price_point_id',
        "price_point_handle": 'price_point_handle',
        "price_point_type": 'price_point_type',
        "price_point_name": 'price_point_name',
        "product_family_id": 'product_family_id',
        "product_family_handle": 'product_family_handle',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "description": 'description',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "subscription": 'subscription',
        "display_on_hosted_page": 'display_on_hosted_page'
    }

    _optionals = [
        'id',
        'name',
        'kind',
        'unit_name',
        'enabled',
        'unit_balance',
        'currency',
        'allocated_quantity',
        'pricing_scheme',
        'component_id',
        'component_handle',
        'subscription_id',
        'recurring',
        'upgrade_charge',
        'downgrade_credit',
        'archived_at',
        'price_point_id',
        'price_point_handle',
        'price_point_type',
        'price_point_name',
        'product_family_id',
        'product_family_handle',
        'created_at',
        'updated_at',
        'use_site_exchange_rate',
        'description',
        'allow_fractional_quantities',
        'subscription',
        'display_on_hosted_page',
    ]

    _nullables = [
        'pricing_scheme',
        'component_handle',
        'upgrade_charge',
        'downgrade_credit',
        'archived_at',
        'price_point_id',
        'price_point_handle',
        'price_point_name',
        'use_site_exchange_rate',
        'description',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 unit_name=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 unit_balance=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 allocated_quantity=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 price_point_handle=APIHelper.SKIP,
                 price_point_type=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 product_family_handle=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 subscription=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP):
        """Constructor for the SubscriptionComponent class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if unit_name is not APIHelper.SKIP:
            self.unit_name = unit_name 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if unit_balance is not APIHelper.SKIP:
            self.unit_balance = unit_balance 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if allocated_quantity is not APIHelper.SKIP:
            self.allocated_quantity = allocated_quantity 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = archived_at 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if price_point_handle is not APIHelper.SKIP:
            self.price_point_handle = price_point_handle 
        if price_point_type is not APIHelper.SKIP:
            self.price_point_type = price_point_type 
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if product_family_handle is not APIHelper.SKIP:
            self.product_family_handle = product_family_handle 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if description is not APIHelper.SKIP:
            self.description = description 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 
        if display_on_hosted_page is not APIHelper.SKIP:
            self.display_on_hosted_page = display_on_hosted_page 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        unit_name = dictionary.get("unit_name") if dictionary.get("unit_name") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        unit_balance = dictionary.get("unit_balance") if dictionary.get("unit_balance") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        allocated_quantity = dictionary.get("allocated_quantity") if dictionary.get("allocated_quantity") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if "pricing_scheme" in dictionary.keys() else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if "component_handle" in dictionary.keys() else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        archived_at = dictionary.get("archived_at") if "archived_at" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if "price_point_id" in dictionary.keys() else APIHelper.SKIP
        price_point_handle = dictionary.get("price_point_handle") if "price_point_handle" in dictionary.keys() else APIHelper.SKIP
        price_point_type = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionComponentPricePointType'), dictionary.get('price_point_type'), False) if dictionary.get('price_point_type') is not None else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if "price_point_name" in dictionary.keys() else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        product_family_handle = dictionary.get("product_family_handle") if dictionary.get("product_family_handle") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        subscription = SubscriptionComponentSubscription.from_dictionary(dictionary.get('subscription')) if 'subscription' in dictionary.keys() else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   kind,
                   unit_name,
                   enabled,
                   unit_balance,
                   currency,
                   allocated_quantity,
                   pricing_scheme,
                   component_id,
                   component_handle,
                   subscription_id,
                   recurring,
                   upgrade_charge,
                   downgrade_credit,
                   archived_at,
                   price_point_id,
                   price_point_handle,
                   price_point_type,
                   price_point_name,
                   product_family_id,
                   product_family_handle,
                   created_at,
                   updated_at,
                   use_site_exchange_rate,
                   description,
                   allow_fractional_quantities,
                   subscription,
                   display_on_hosted_page)
