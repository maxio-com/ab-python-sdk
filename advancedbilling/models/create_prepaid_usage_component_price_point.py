# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme


class CreatePrepaidUsageComponentPricePoint(object):

    """Implementation of the 'Create Prepaid Usage Component Price Point' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): TODO: type description here.
        overage_pricing (OveragePricing): TODO: type description here.
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site.
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
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "overage_pricing": 'overage_pricing',
        "handle": 'handle',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "rollover_prepaid_remainder": 'rollover_prepaid_remainder',
        "renew_prepaid_allocation": 'renew_prepaid_allocation',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit'
    }

    _optionals = [
        'handle',
        'use_site_exchange_rate',
        'rollover_prepaid_remainder',
        'renew_prepaid_allocation',
        'expiration_interval',
        'expiration_interval_unit',
    ]

    def __init__(self,
                 name=None,
                 pricing_scheme=None,
                 prices=None,
                 overage_pricing=None,
                 handle=APIHelper.SKIP,
                 use_site_exchange_rate=True,
                 rollover_prepaid_remainder=APIHelper.SKIP,
                 renew_prepaid_allocation=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP):
        """Constructor for the CreatePrepaidUsageComponentPricePoint class"""

        # Initialize members of the class
        self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        self.pricing_scheme = pricing_scheme 
        self.prices = prices 
        self.overage_pricing = overage_pricing 
        self.use_site_exchange_rate = use_site_exchange_rate 
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else None
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else None
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        overage_pricing = OveragePricing.from_dictionary(dictionary.get('overage_pricing')) if dictionary.get('overage_pricing') else None
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if dictionary.get("use_site_exchange_rate") else True
        rollover_prepaid_remainder = dictionary.get("rollover_prepaid_remainder") if "rollover_prepaid_remainder" in dictionary.keys() else APIHelper.SKIP
        renew_prepaid_allocation = dictionary.get("renew_prepaid_allocation") if "renew_prepaid_allocation" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if dictionary.get("expiration_interval") else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if dictionary.get("expiration_interval_unit") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   pricing_scheme,
                   prices,
                   overage_pricing,
                   handle,
                   use_site_exchange_rate,
                   rollover_prepaid_remainder,
                   renew_prepaid_allocation,
                   expiration_interval,
                   expiration_interval_unit)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.pricing_scheme, type_callable=lambda value: PricingScheme.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.prices, type_callable=lambda value: Price.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.overage_pricing, type_callable=lambda value: OveragePricing.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('pricing_scheme'), type_callable=lambda value: PricingScheme.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('prices'), type_callable=lambda value: Price.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('overage_pricing'), type_callable=lambda value: OveragePricing.validate(value))
