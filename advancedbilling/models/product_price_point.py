# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.currency_price import CurrencyPrice


class ProductPricePoint(object):

    """Implementation of the 'Product Price Point' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (str): The product price point name
        handle (str): The product price point API handle
        price_in_cents (long|int): The product price point price, in integer
            cents
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this product price
            point would renew every 30 days
        interval_unit (IntervalUnit): A string representing the interval unit
            for this product price point, either month or day
        trial_price_in_cents (long|int): The product price point trial price,
            in integer cents
        trial_interval (int): The numerical trial interval. i.e. an interval
            of ‘30’ coupled with a trial_interval_unit of day would mean this
            product price point trial would last 30 days
        trial_interval_unit (IntervalUnit): A string representing the trial
            interval unit for this product price point, either month or day
        trial_type (str): TODO: type description here.
        introductory_offer (bool): reserved for future use
        initial_charge_in_cents (long|int): The product price point initial
            charge, in integer cents
        initial_charge_after_trial (bool): TODO: type description here.
        expiration_interval (int): The numerical expiration interval. i.e. an
            expiration_interval of ‘30’ coupled with an
            expiration_interval_unit of day would mean this product price
            point would expire after 30 days
        expiration_interval_unit (IntervalUnit): A string representing the
            expiration interval unit for this product price point, either
            month or day
        product_id (int): The product id this price point belongs to
        archived_at (datetime): Timestamp indicating when this price point was
            archived
        created_at (datetime): Timestamp indicating when this price point was
            created
        updated_at (datetime): Timestamp indicating when this price point was
            last updated
        use_site_exchange_rate (bool): Whether or not to use the site's
            exchange rate or define your own pricing when your site has
            multiple currencies defined.
        mtype (PricePointType): The type of price point
        tax_included (bool): Whether or not the price point includes tax
        subscription_id (int): The subscription id this price point belongs
            to
        currency_prices (List[CurrencyPrice]): An array of currency pricing
            data is available when multiple currencies are defined for the
            site. It varies based on the use_site_exchange_rate setting for
            the price point. This parameter is present only in the response of
            read endpoints, after including the appropriate query parameter.

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
        "subscription_id": 'subscription_id',
        "currency_prices": 'currency_prices'
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
        'currency_prices',
    ]

    _nullables = [
        'archived_at',
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
                 subscription_id=APIHelper.SKIP,
                 currency_prices=APIHelper.SKIP,
                 additional_properties={}):
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
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if currency_prices is not APIHelper.SKIP:
            self.currency_prices = currency_prices 

        # Add additional model properties to the instance
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
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if "subscription_id" in dictionary.keys() else APIHelper.SKIP
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [CurrencyPrice.from_dictionary(x) for x in dictionary.get('currency_prices')]
        else:
            currency_prices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
                   subscription_id,
                   currency_prices,
                   dictionary)
