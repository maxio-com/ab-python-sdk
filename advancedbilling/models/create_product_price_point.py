# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateProductPricePoint(object):

    """Implementation of the 'Create Product Price Point' model.

    TODO: type model description here.

    Attributes:
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
            product price point trial would last 30 days.
        trial_interval_unit (IntervalUnit): A string representing the trial
            interval unit for this product price point, either month or day
        trial_type (str): TODO: type description here.
        initial_charge_in_cents (long|int): The product price point initial
            charge, in integer cents
        initial_charge_after_trial (bool): TODO: type description here.
        expiration_interval (int): The numerical expiration interval. i.e. an
            expiration_interval of ‘30’ coupled with an
            expiration_interval_unit of day would mean this product price
            point would expire after 30 days.
        expiration_interval_unit (ExpirationIntervalUnit): A string
            representing the expiration interval unit for this product price
            point, either month, day or never
        use_site_exchange_rate (bool): Whether or not to use the site's
            exchange rate or define your own pricing when your site has
            multiple currencies defined.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "price_in_cents": 'price_in_cents',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "handle": 'handle',
        "trial_price_in_cents": 'trial_price_in_cents',
        "trial_interval": 'trial_interval',
        "trial_interval_unit": 'trial_interval_unit',
        "trial_type": 'trial_type',
        "initial_charge_in_cents": 'initial_charge_in_cents',
        "initial_charge_after_trial": 'initial_charge_after_trial',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit',
        "use_site_exchange_rate": 'use_site_exchange_rate'
    }

    _optionals = [
        'handle',
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'trial_type',
        'initial_charge_in_cents',
        'initial_charge_after_trial',
        'expiration_interval',
        'expiration_interval_unit',
        'use_site_exchange_rate',
    ]

    _nullables = [
        'expiration_interval_unit',
    ]

    def __init__(self,
                 name=None,
                 price_in_cents=None,
                 interval=None,
                 interval_unit=None,
                 handle=APIHelper.SKIP,
                 trial_price_in_cents=APIHelper.SKIP,
                 trial_interval=APIHelper.SKIP,
                 trial_interval_unit=APIHelper.SKIP,
                 trial_type=APIHelper.SKIP,
                 initial_charge_in_cents=APIHelper.SKIP,
                 initial_charge_after_trial=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 use_site_exchange_rate=True,
                 additional_properties={}):
        """Constructor for the CreateProductPricePoint class"""

        # Initialize members of the class
        self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        self.price_in_cents = price_in_cents 
        self.interval = interval 
        self.interval_unit = interval_unit 
        if trial_price_in_cents is not APIHelper.SKIP:
            self.trial_price_in_cents = trial_price_in_cents 
        if trial_interval is not APIHelper.SKIP:
            self.trial_interval = trial_interval 
        if trial_interval_unit is not APIHelper.SKIP:
            self.trial_interval_unit = trial_interval_unit 
        if trial_type is not APIHelper.SKIP:
            self.trial_type = trial_type 
        if initial_charge_in_cents is not APIHelper.SKIP:
            self.initial_charge_in_cents = initial_charge_in_cents 
        if initial_charge_after_trial is not APIHelper.SKIP:
            self.initial_charge_after_trial = initial_charge_after_trial 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 
        self.use_site_exchange_rate = use_site_exchange_rate 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else None
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else None
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        trial_price_in_cents = dictionary.get("trial_price_in_cents") if dictionary.get("trial_price_in_cents") else APIHelper.SKIP
        trial_interval = dictionary.get("trial_interval") if dictionary.get("trial_interval") else APIHelper.SKIP
        trial_interval_unit = dictionary.get("trial_interval_unit") if dictionary.get("trial_interval_unit") else APIHelper.SKIP
        trial_type = dictionary.get("trial_type") if dictionary.get("trial_type") else APIHelper.SKIP
        initial_charge_in_cents = dictionary.get("initial_charge_in_cents") if dictionary.get("initial_charge_in_cents") else APIHelper.SKIP
        initial_charge_after_trial = dictionary.get("initial_charge_after_trial") if "initial_charge_after_trial" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if dictionary.get("expiration_interval") else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if "expiration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if dictionary.get("use_site_exchange_rate") else True
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   price_in_cents,
                   interval,
                   interval_unit,
                   handle,
                   trial_price_in_cents,
                   trial_interval,
                   trial_interval_unit,
                   trial_type,
                   initial_charge_in_cents,
                   initial_charge_after_trial,
                   expiration_interval,
                   expiration_interval_unit,
                   use_site_exchange_rate,
                   dictionary)
