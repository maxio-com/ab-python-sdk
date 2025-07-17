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

    Attributes:
        id (int): The model property of type int.
        mtype (PricePointType): Price point type. We expose the following
            types: 1. **default**: a price point that is marked as a default
            price for a certain product. 2. **custom**: a custom price point.
            3. **catalog**: a price point that is **not** marked as a default
            price for a certain product and is **not** a custom one.
        default (bool): Note: Refer to type attribute instead
        name (str): The model property of type str.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        component_id (int): The model property of type int.
        handle (str): The model property of type str.
        archived_at (datetime): The model property of type datetime.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        prices (List[ComponentPrice]): The model property of type
            List[ComponentPrice].
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site. Defaults to true during
            creation.
        subscription_id (int): (only used for Custom Pricing - ie. when the
            price point's type is `custom`) The id of the subscription that
            the custom price point is for.
        tax_included (bool): The model property of type bool.
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        currency_prices (List[ComponentCurrencyPrice]): An array of currency
            pricing data is available when multiple currencies are defined for
            the site. It varies based on the use_site_exchange_rate setting
            for the price point. This parameter is present only in the
            response of read endpoints, after including the appropriate query
            parameter.
        overage_prices (List[ComponentPrice]): Applicable only to prepaid
            usage components. An array of overage price brackets.
        overage_pricing_scheme (PricingScheme): Applicable only to prepaid
            usage components. Pricing scheme for overage pricing.
        renew_prepaid_allocation (bool): Applicable only to prepaid usage
            components. Boolean which controls whether or not the allocated
            quantity should be renewed at the beginning of each period.
        rollover_prepaid_remainder (bool): Applicable only to prepaid usage
            components. Boolean which controls whether or not remaining units
            should be rolled over to the next period.
        expiration_interval (int): Applicable only to prepaid usage components
            where rollover_prepaid_remainder is true. The number of
            `expiration_interval_unit`s after which rollover amounts should
            expire.
        expiration_interval_unit (ExpirationIntervalUnit): Applicable only to
            prepaid usage components where rollover_prepaid_remainder is true.
            A string representing the expiration interval unit for this
            component, either month or day.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        "currency_prices": 'currency_prices',
        "overage_prices": 'overage_prices',
        "overage_pricing_scheme": 'overage_pricing_scheme',
        "renew_prepaid_allocation": 'renew_prepaid_allocation',
        "rollover_prepaid_remainder": 'rollover_prepaid_remainder',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit'
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
        'overage_prices',
        'overage_pricing_scheme',
        'renew_prepaid_allocation',
        'rollover_prepaid_remainder',
        'expiration_interval',
        'expiration_interval_unit',
    ]

    _nullables = [
        'handle',
        'archived_at',
        'interval',
        'interval_unit',
        'expiration_interval',
        'expiration_interval_unit',
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
                 use_site_exchange_rate=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 tax_included=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 currency_prices=APIHelper.SKIP,
                 overage_prices=APIHelper.SKIP,
                 overage_pricing_scheme=APIHelper.SKIP,
                 renew_prepaid_allocation=APIHelper.SKIP,
                 rollover_prepaid_remainder=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 additional_properties=None):
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
        if use_site_exchange_rate is not APIHelper.SKIP:
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
        if overage_prices is not APIHelper.SKIP:
            self.overage_prices = overage_prices 
        if overage_pricing_scheme is not APIHelper.SKIP:
            self.overage_pricing_scheme = overage_pricing_scheme 
        if renew_prepaid_allocation is not APIHelper.SKIP:
            self.renew_prepaid_allocation = renew_prepaid_allocation 
        if rollover_prepaid_remainder is not APIHelper.SKIP:
            self.rollover_prepaid_remainder = rollover_prepaid_remainder 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        default = dictionary.get("default") if "default" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        handle = dictionary.get("handle") if "handle" in dictionary.keys() else APIHelper.SKIP
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
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        interval = dictionary.get("interval") if "interval" in dictionary.keys() else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [ComponentCurrencyPrice.from_dictionary(x) for x in dictionary.get('currency_prices')]
        else:
            currency_prices = APIHelper.SKIP
        overage_prices = None
        if dictionary.get('overage_prices') is not None:
            overage_prices = [ComponentPrice.from_dictionary(x) for x in dictionary.get('overage_prices')]
        else:
            overage_prices = APIHelper.SKIP
        overage_pricing_scheme = dictionary.get("overage_pricing_scheme") if dictionary.get("overage_pricing_scheme") else APIHelper.SKIP
        renew_prepaid_allocation = dictionary.get("renew_prepaid_allocation") if "renew_prepaid_allocation" in dictionary.keys() else APIHelper.SKIP
        rollover_prepaid_remainder = dictionary.get("rollover_prepaid_remainder") if "rollover_prepaid_remainder" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if "expiration_interval" in dictionary.keys() else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if "expiration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   currency_prices,
                   overage_prices,
                   overage_pricing_scheme,
                   renew_prepaid_allocation,
                   rollover_prepaid_remainder,
                   expiration_interval,
                   expiration_interval_unit,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'default={(self.default if hasattr(self, "default") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'pricing_scheme={(self.pricing_scheme if hasattr(self, "pricing_scheme") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!r}, '
                f'archived_at={(self.archived_at if hasattr(self, "archived_at") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'prices={(self.prices if hasattr(self, "prices") else None)!r}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'tax_included={(self.tax_included if hasattr(self, "tax_included") else None)!r}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!r}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!r}, '
                f'currency_prices={(self.currency_prices if hasattr(self, "currency_prices") else None)!r}, '
                f'overage_prices={(self.overage_prices if hasattr(self, "overage_prices") else None)!r}, '
                f'overage_pricing_scheme={(self.overage_pricing_scheme if hasattr(self, "overage_pricing_scheme") else None)!r}, '
                f'renew_prepaid_allocation={(self.renew_prepaid_allocation if hasattr(self, "renew_prepaid_allocation") else None)!r}, '
                f'rollover_prepaid_remainder={(self.rollover_prepaid_remainder if hasattr(self, "rollover_prepaid_remainder") else None)!r}, '
                f'expiration_interval={(self.expiration_interval if hasattr(self, "expiration_interval") else None)!r}, '
                f'expiration_interval_unit={(self.expiration_interval_unit if hasattr(self, "expiration_interval_unit") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'default={(self.default if hasattr(self, "default") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'pricing_scheme={(self.pricing_scheme if hasattr(self, "pricing_scheme") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!s}, '
                f'archived_at={(self.archived_at if hasattr(self, "archived_at") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'prices={(self.prices if hasattr(self, "prices") else None)!s}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'tax_included={(self.tax_included if hasattr(self, "tax_included") else None)!s}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!s}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!s}, '
                f'currency_prices={(self.currency_prices if hasattr(self, "currency_prices") else None)!s}, '
                f'overage_prices={(self.overage_prices if hasattr(self, "overage_prices") else None)!s}, '
                f'overage_pricing_scheme={(self.overage_pricing_scheme if hasattr(self, "overage_pricing_scheme") else None)!s}, '
                f'renew_prepaid_allocation={(self.renew_prepaid_allocation if hasattr(self, "renew_prepaid_allocation") else None)!s}, '
                f'rollover_prepaid_remainder={(self.rollover_prepaid_remainder if hasattr(self, "rollover_prepaid_remainder") else None)!s}, '
                f'expiration_interval={(self.expiration_interval if hasattr(self, "expiration_interval") else None)!s}, '
                f'expiration_interval_unit={(self.expiration_interval_unit if hasattr(self, "expiration_interval_unit") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
