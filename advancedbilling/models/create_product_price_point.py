# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateProductPricePoint(object):

    """Implementation of the 'Create Product Price Point' model.

    Attributes:
        name (str): The product price point name
        handle (str): The product price point API handle
        price_in_cents (int): The product price point price, in integer cents
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this product price
            point would renew every 30 days
        interval_unit (IntervalUnit): A string representing the interval unit
            for this product price point, either month or day
        trial_price_in_cents (int): The product price point trial price, in
            integer cents
        trial_interval (int): The numerical trial interval. i.e. an interval
            of ‘30’ coupled with a trial_interval_unit of day would mean this
            product price point trial would last 30 days.
        trial_interval_unit (IntervalUnit): A string representing the trial
            interval unit for this product price point, either month or day
        trial_type (str): The model property of type str.
        initial_charge_in_cents (int): The product price point initial charge,
            in integer cents
        initial_charge_after_trial (bool): The model property of type bool.
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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!r}, '
                f'price_in_cents={self.price_in_cents!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'trial_price_in_cents={(self.trial_price_in_cents if hasattr(self, "trial_price_in_cents") else None)!r}, '
                f'trial_interval={(self.trial_interval if hasattr(self, "trial_interval") else None)!r}, '
                f'trial_interval_unit={(self.trial_interval_unit if hasattr(self, "trial_interval_unit") else None)!r}, '
                f'trial_type={(self.trial_type if hasattr(self, "trial_type") else None)!r}, '
                f'initial_charge_in_cents={(self.initial_charge_in_cents if hasattr(self, "initial_charge_in_cents") else None)!r}, '
                f'initial_charge_after_trial={(self.initial_charge_after_trial if hasattr(self, "initial_charge_after_trial") else None)!r}, '
                f'expiration_interval={(self.expiration_interval if hasattr(self, "expiration_interval") else None)!r}, '
                f'expiration_interval_unit={(self.expiration_interval_unit if hasattr(self, "expiration_interval_unit") else None)!r}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!s}, '
                f'price_in_cents={self.price_in_cents!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'trial_price_in_cents={(self.trial_price_in_cents if hasattr(self, "trial_price_in_cents") else None)!s}, '
                f'trial_interval={(self.trial_interval if hasattr(self, "trial_interval") else None)!s}, '
                f'trial_interval_unit={(self.trial_interval_unit if hasattr(self, "trial_interval_unit") else None)!s}, '
                f'trial_type={(self.trial_type if hasattr(self, "trial_type") else None)!s}, '
                f'initial_charge_in_cents={(self.initial_charge_in_cents if hasattr(self, "initial_charge_in_cents") else None)!s}, '
                f'initial_charge_after_trial={(self.initial_charge_after_trial if hasattr(self, "initial_charge_after_trial") else None)!s}, '
                f'expiration_interval={(self.expiration_interval if hasattr(self, "expiration_interval") else None)!s}, '
                f'expiration_interval_unit={(self.expiration_interval_unit if hasattr(self, "expiration_interval_unit") else None)!s}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
