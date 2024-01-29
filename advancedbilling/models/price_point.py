# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.price import Price


class PricePoint(object):

    """Implementation of the 'PricePoint' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): TODO: type description here.
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site.
        tax_included (bool): Whether or not the price point includes tax
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this price point
            would renew every 30 days. This property is only available for
            sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this price point, either month or day. This property is only
            available for sites with Multifrequency enabled.
        overage_pricing (OveragePricing): TODO: type description here.
        rollover_prepaid_remainder (bool): Boolean which controls whether or
            not remaining units should be rolled over to the next period
        renew_prepaid_allocation (bool): Boolean which controls whether or not
            the allocated quantity should be renewed at the beginning of each
            period
        expiration_interval (float): (only for prepaid usage components where
            rollover_prepaid_remainder is true) The number of
            `expiration_interval_unit`s after which rollover amounts should
            expire
        expiration_interval_unit (IntervalUnit): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "tax_included": 'tax_included',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "overage_pricing": 'overage_pricing',
        "rollover_prepaid_remainder": 'rollover_prepaid_remainder',
        "renew_prepaid_allocation": 'renew_prepaid_allocation',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit'
    }

    _optionals = [
        'name',
        'handle',
        'pricing_scheme',
        'prices',
        'use_site_exchange_rate',
        'tax_included',
        'interval',
        'interval_unit',
        'overage_pricing',
        'rollover_prepaid_remainder',
        'renew_prepaid_allocation',
        'expiration_interval',
        'expiration_interval_unit',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 use_site_exchange_rate=True,
                 tax_included=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 overage_pricing=APIHelper.SKIP,
                 rollover_prepaid_remainder=APIHelper.SKIP,
                 renew_prepaid_allocation=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP):
        """Constructor for the PricePoint class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        self.use_site_exchange_rate = use_site_exchange_rate 
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if overage_pricing is not APIHelper.SKIP:
            self.overage_pricing = overage_pricing 
        if rollover_prepaid_remainder is not APIHelper.SKIP:
            self.rollover_prepaid_remainder = rollover_prepaid_remainder 
        if renew_prepaid_allocation is not APIHelper.SKIP:
            self.renew_prepaid_allocation = renew_prepaid_allocation 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if dictionary.get("use_site_exchange_rate") else True
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        overage_pricing = OveragePricing.from_dictionary(dictionary.get('overage_pricing')) if 'overage_pricing' in dictionary.keys() else APIHelper.SKIP
        rollover_prepaid_remainder = dictionary.get("rollover_prepaid_remainder") if "rollover_prepaid_remainder" in dictionary.keys() else APIHelper.SKIP
        renew_prepaid_allocation = dictionary.get("renew_prepaid_allocation") if "renew_prepaid_allocation" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if dictionary.get("expiration_interval") else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if dictionary.get("expiration_interval_unit") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   handle,
                   pricing_scheme,
                   prices,
                   use_site_exchange_rate,
                   tax_included,
                   interval,
                   interval_unit,
                   overage_pricing,
                   rollover_prepaid_remainder,
                   renew_prepaid_allocation,
                   expiration_interval,
                   expiration_interval_unit)
