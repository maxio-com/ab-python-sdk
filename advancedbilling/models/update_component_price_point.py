# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.update_price import UpdatePrice


class UpdateComponentPricePoint(object):

    """Implementation of the 'Update Component Price Point' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site.
        tax_included (bool): Whether or not the price point includes tax
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        prices (List[UpdatePrice]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "pricing_scheme": 'pricing_scheme',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "tax_included": 'tax_included',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "prices": 'prices'
    }

    _optionals = [
        'name',
        'handle',
        'pricing_scheme',
        'use_site_exchange_rate',
        'tax_included',
        'interval',
        'interval_unit',
        'prices',
    ]

    _nullables = [
        'interval_unit',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 tax_included=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the UpdateComponentPricePoint class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if prices is not APIHelper.SKIP:
            self.prices = prices 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [UpdatePrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   handle,
                   pricing_scheme,
                   use_site_exchange_rate,
                   tax_included,
                   interval,
                   interval_unit,
                   prices,
                   dictionary)
