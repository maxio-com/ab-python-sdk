# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomPriceUsedForSubscriptionCreateUpdate(object):

    """Implementation of the 'Custom price used for Subscription Create/Update' model.

    (Optional) Used in place of `product_price_point_id` to define a custom
    price point unique to the subscription

    Attributes:
        name (str): (Optional)
        handle (str): (Optional)
        price_in_cents (str | int | None): Required if using `custom_price`
            attribute.
        interval (str | int | None): Required if using `custom_price`
            attribute.
        interval_unit (IntervalUnit | None): Required if using `custom_price`
            attribute.
        trial_price_in_cents (str | int | None): (Optional)
        trial_interval (str | int | None): (Optional)
        trial_interval_unit (IntervalUnit | None): (Optional)
        initial_charge_in_cents (str | int | None): (Optional)
        initial_charge_after_trial (bool): (Optional)
        expiration_interval (str | int | None): (Optional)
        expiration_interval_unit (IntervalUnit | None): (Optional)
        tax_included (bool): (Optional)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "price_in_cents": 'price_in_cents',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "trial_price_in_cents": 'trial_price_in_cents',
        "trial_interval": 'trial_interval',
        "trial_interval_unit": 'trial_interval_unit',
        "initial_charge_in_cents": 'initial_charge_in_cents',
        "initial_charge_after_trial": 'initial_charge_after_trial',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit',
        "tax_included": 'tax_included'
    }

    _optionals = [
        'name',
        'handle',
        'price_in_cents',
        'interval',
        'interval_unit',
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'initial_charge_in_cents',
        'initial_charge_after_trial',
        'expiration_interval',
        'expiration_interval_unit',
        'tax_included',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 trial_price_in_cents=APIHelper.SKIP,
                 trial_interval=APIHelper.SKIP,
                 trial_interval_unit=APIHelper.SKIP,
                 initial_charge_in_cents=APIHelper.SKIP,
                 initial_charge_after_trial=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 tax_included=APIHelper.SKIP):
        """Constructor for the CustomPriceUsedForSubscriptionCreateUpdate class"""

        # Initialize members of the class
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
        if initial_charge_in_cents is not APIHelper.SKIP:
            self.initial_charge_in_cents = initial_charge_in_cents 
        if initial_charge_after_trial is not APIHelper.SKIP:
            self.initial_charge_after_trial = initial_charge_after_trial 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 
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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        price_in_cents = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdatePriceInCents'), dictionary.get('price_in_cents'), False) if dictionary.get('price_in_cents') is not None else APIHelper.SKIP
        interval = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateInterval'), dictionary.get('interval'), False) if dictionary.get('interval') is not None else APIHelper.SKIP
        interval_unit = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateIntervalUnit'), dictionary.get('interval_unit'), False) if dictionary.get('interval_unit') is not None else APIHelper.SKIP
        trial_price_in_cents = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateTrialPriceInCents'), dictionary.get('trial_price_in_cents'), False) if dictionary.get('trial_price_in_cents') is not None else APIHelper.SKIP
        trial_interval = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateTrialInterval'), dictionary.get('trial_interval'), False) if dictionary.get('trial_interval') is not None else APIHelper.SKIP
        trial_interval_unit = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateTrialIntervalUnit'), dictionary.get('trial_interval_unit'), False) if dictionary.get('trial_interval_unit') is not None else APIHelper.SKIP
        initial_charge_in_cents = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateInitialChargeInCents'), dictionary.get('initial_charge_in_cents'), False) if dictionary.get('initial_charge_in_cents') is not None else APIHelper.SKIP
        initial_charge_after_trial = dictionary.get("initial_charge_after_trial") if "initial_charge_after_trial" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateExpirationInterval'), dictionary.get('expiration_interval'), False) if dictionary.get('expiration_interval') is not None else APIHelper.SKIP
        expiration_interval_unit = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomPriceUsedForSubscriptionCreateUpdateExpirationIntervalUnit'), dictionary.get('expiration_interval_unit'), False) if dictionary.get('expiration_interval_unit') is not None else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   handle,
                   price_in_cents,
                   interval,
                   interval_unit,
                   trial_price_in_cents,
                   trial_interval,
                   trial_interval_unit,
                   initial_charge_in_cents,
                   initial_charge_after_trial,
                   expiration_interval,
                   expiration_interval_unit,
                   tax_included)
