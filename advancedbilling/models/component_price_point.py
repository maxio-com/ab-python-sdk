# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price_point_price import ComponentPricePointPrice


class ComponentPricePoint(object):

    """Implementation of the 'Component Price Point' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        mtype (PricePointType): Price point type. We expose the following
            types: 1. **default**: a price point that is marked as a default
            price for a certain product. 2. **custom**: a custom price point.
            3. **catalog**: a price point that is **not** marked as a default
            price for a certain product and is **not** a custom one.
        default (bool): Note: Refer to type attribute instead
        name (str): TODO: type description here.
        pricing_scheme (str): TODO: type description here.
        component_id (int): TODO: type description here.
        handle (str): TODO: type description here.
        archived_at (str): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
        prices (List[ComponentPricePointPrice]): TODO: type description here.
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site.
        subscription_id (int): (only used for Custom Pricing - ie. when the
            price point's type is `custom`) The id of the subscription that
            the custom price point is for.
        tax_included (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "mtype": 'type',
        "default": 'default',
        "name": 'name',
        "pricing_scheme": 'pricing_scheme',
        "component_id": 'component_id',
        "handle": 'handle',
        "archived_at": 'archived_at',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "prices": 'prices',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "subscription_id": 'subscription_id',
        "tax_included": 'tax_included'
    }

    _optionals = [
        'id',
        'mtype',
        'default',
        'name',
        'pricing_scheme',
        'component_id',
        'handle',
        'archived_at',
        'created_at',
        'updated_at',
        'prices',
        'use_site_exchange_rate',
        'subscription_id',
        'tax_included',
    ]

    _nullables = [
        'archived_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 default=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 use_site_exchange_rate=True,
                 subscription_id=APIHelper.SKIP,
                 tax_included=APIHelper.SKIP):
        """Constructor for the ComponentPricePoint class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if default is not APIHelper.SKIP:
            self.default = default 
        if name is not APIHelper.SKIP:
            self.name = name 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = archived_at 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        self.use_site_exchange_rate = use_site_exchange_rate 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 

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
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        default = dictionary.get("default") if "default" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        archived_at = dictionary.get("archived_at") if "archived_at" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [ComponentPricePointPrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if dictionary.get("use_site_exchange_rate") else True
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   mtype,
                   default,
                   name,
                   pricing_scheme,
                   component_id,
                   handle,
                   archived_at,
                   created_at,
                   updated_at,
                   prices,
                   use_site_exchange_rate,
                   subscription_id,
                   tax_included)
