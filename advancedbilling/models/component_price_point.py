# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_currency_price import ComponentCurrencyPrice
from advancedbilling.models.component_price import ComponentPrice


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
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        component_id (int): TODO: type description here.
        handle (str): TODO: type description here.
        archived_at (datetime): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        prices (List[ComponentPrice]): TODO: type description here.
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site.
        subscription_id (int): (only used for Custom Pricing - ie. when the
            price point's type is `custom`) The id of the subscription that
            the custom price point is for.
        tax_included (bool): TODO: type description here.
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit | None): A string representing the
            interval unit for this component price point, either month or day.
            This property is only available for sites with Multifrequency
            enabled.
        currency_prices (List[ComponentCurrencyPrice]): An array of currency
            pricing data is available when multiple currencies are defined for
            the site. It varies based on the use_site_exchange_rate setting
            for the price point. This parameter is present only in the
            response of read endpoints, after including the appropriate query
            parameter.

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
        "tax_included": 'tax_included',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "currency_prices": 'currency_prices'
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
        'interval',
        'interval_unit',
        'currency_prices',
    ]

    _nullables = [
        'archived_at',
        'interval',
        'interval_unit',
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
                 tax_included=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 currency_prices=APIHelper.SKIP):
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
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        self.use_site_exchange_rate = use_site_exchange_rate 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if currency_prices is not APIHelper.SKIP:
            self.currency_prices = currency_prices 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        default = dictionary.get("default") if "default" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [ComponentPrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if dictionary.get("use_site_exchange_rate") else True
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        interval = dictionary.get("interval") if "interval" in dictionary.keys() else APIHelper.SKIP
        if 'interval_unit' in dictionary.keys():
            interval_unit = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ComponentPricePointIntervalUnit'), dictionary.get('interval_unit'), False) if dictionary.get('interval_unit') is not None else None
        else:
            interval_unit = APIHelper.SKIP
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [ComponentCurrencyPrice.from_dictionary(x) for x in dictionary.get('currency_prices')]
        else:
            currency_prices = APIHelper.SKIP
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
                   tax_included,
                   interval,
                   interval_unit,
                   currency_prices)
