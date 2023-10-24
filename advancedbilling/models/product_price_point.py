# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProductPricePoint(object):

    """Implementation of the 'Product Price Point' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        price_in_cents (int): TODO: type description here.
        interval (int): TODO: type description here.
        interval_unit (str): TODO: type description here.
        trial_price_in_cents (int): TODO: type description here.
        trial_interval (int): TODO: type description here.
        trial_interval_unit (str): TODO: type description here.
        trial_type (str): TODO: type description here.
        introductory_offer (bool): reserved for future use
        initial_charge_in_cents (int): TODO: type description here.
        initial_charge_after_trial (bool): TODO: type description here.
        expiration_interval (int): TODO: type description here.
        expiration_interval_unit (str): TODO: type description here.
        product_id (int): TODO: type description here.
        archived_at (str): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
        use_site_exchange_rate (bool): Whether or not to use the site's
            exchange rate or define your own pricing when your site has
            multiple currencies defined.
        mtype (PricePointType): Price point type. We expose the following
            types: 1. **default**: a price point that is marked as a default
            price for a certain product. 2. **custom**: a custom price point.
            3. **catalog**: a price point that is **not** marked as a default
            price for a certain product and is **not** a custom one.
        tax_included (bool): TODO: type description here.
        subscription_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "handle": 'handle',
        "price_in_cents": 'price_in_cents',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "trial_price_in_cents": 'trial_price_in_cents',
        "trial_interval": 'trial_interval',
        "trial_interval_unit": 'trial_interval_unit',
        "trial_type": 'trial_type',
        "introductory_offer": 'introductory_offer',
        "initial_charge_in_cents": 'initial_charge_in_cents',
        "initial_charge_after_trial": 'initial_charge_after_trial',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit',
        "product_id": 'product_id',
        "archived_at": 'archived_at',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "mtype": 'type',
        "tax_included": 'tax_included',
        "subscription_id": 'subscription_id'
    }

    _optionals = [
        'id',
        'name',
        'handle',
        'price_in_cents',
        'interval',
        'interval_unit',
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'trial_type',
        'introductory_offer',
        'initial_charge_in_cents',
        'initial_charge_after_trial',
        'expiration_interval',
        'expiration_interval_unit',
        'product_id',
        'archived_at',
        'created_at',
        'updated_at',
        'use_site_exchange_rate',
        'mtype',
        'tax_included',
        'subscription_id',
    ]

    _nullables = [
        'subscription_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 trial_price_in_cents=APIHelper.SKIP,
                 trial_interval=APIHelper.SKIP,
                 trial_interval_unit=APIHelper.SKIP,
                 trial_type=APIHelper.SKIP,
                 introductory_offer=APIHelper.SKIP,
                 initial_charge_in_cents=APIHelper.SKIP,
                 initial_charge_after_trial=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 tax_included=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP):
        """Constructor for the ProductPricePoint class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if price_in_cents is not APIHelper.SKIP:
            self.price_in_cents = price_in_cents 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if trial_price_in_cents is not APIHelper.SKIP:
            self.trial_price_in_cents = trial_price_in_cents 
        if trial_interval is not APIHelper.SKIP:
            self.trial_interval = trial_interval 
        if trial_interval_unit is not APIHelper.SKIP:
            self.trial_interval_unit = trial_interval_unit 
        if trial_type is not APIHelper.SKIP:
            self.trial_type = trial_type 
        if introductory_offer is not APIHelper.SKIP:
            self.introductory_offer = introductory_offer 
        if initial_charge_in_cents is not APIHelper.SKIP:
            self.initial_charge_in_cents = initial_charge_in_cents 
        if initial_charge_after_trial is not APIHelper.SKIP:
            self.initial_charge_after_trial = initial_charge_after_trial 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = archived_at 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 

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
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        trial_price_in_cents = dictionary.get("trial_price_in_cents") if dictionary.get("trial_price_in_cents") else APIHelper.SKIP
        trial_interval = dictionary.get("trial_interval") if dictionary.get("trial_interval") else APIHelper.SKIP
        trial_interval_unit = dictionary.get("trial_interval_unit") if dictionary.get("trial_interval_unit") else APIHelper.SKIP
        trial_type = dictionary.get("trial_type") if dictionary.get("trial_type") else APIHelper.SKIP
        introductory_offer = dictionary.get("introductory_offer") if "introductory_offer" in dictionary.keys() else APIHelper.SKIP
        initial_charge_in_cents = dictionary.get("initial_charge_in_cents") if dictionary.get("initial_charge_in_cents") else APIHelper.SKIP
        initial_charge_after_trial = dictionary.get("initial_charge_after_trial") if "initial_charge_after_trial" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if dictionary.get("expiration_interval") else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if dictionary.get("expiration_interval_unit") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        archived_at = dictionary.get("archived_at") if dictionary.get("archived_at") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if "subscription_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   handle,
                   price_in_cents,
                   interval,
                   interval_unit,
                   trial_price_in_cents,
                   trial_interval,
                   trial_interval_unit,
                   trial_type,
                   introductory_offer,
                   initial_charge_in_cents,
                   initial_charge_after_trial,
                   expiration_interval,
                   expiration_interval_unit,
                   product_id,
                   archived_at,
                   created_at,
                   updated_at,
                   use_site_exchange_rate,
                   mtype,
                   tax_included,
                   subscription_id)
