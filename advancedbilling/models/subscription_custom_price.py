# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.interval_unit import IntervalUnit


class SubscriptionCustomPrice(object):

    """Implementation of the 'Subscription Custom Price' model.

    (Optional) Used in place of `product_price_point_id` to define a custom
    price point unique to the subscription

    Attributes:
        name (str): (Optional)
        handle (str): (Optional)
        price_in_cents (str | int): Required if using `custom_price` attribute.
        interval (str | int): Required if using `custom_price` attribute.
        interval_unit (IntervalUnit): Required if using `custom_price`
            attribute.
        trial_price_in_cents (str | int | None): (Optional)
        trial_interval (str | int | None): (Optional)
        trial_interval_unit (IntervalUnit): (Optional)
        initial_charge_in_cents (str | int | None): (Optional)
        initial_charge_after_trial (bool): (Optional)
        expiration_interval (str | int | None): (Optional)
        expiration_interval_unit (ExpirationIntervalUnit): (Optional)
        tax_included (bool): (Optional)
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_in_cents": 'price_in_cents',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "name": 'name',
        "handle": 'handle',
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
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'initial_charge_in_cents',
        'initial_charge_after_trial',
        'expiration_interval',
        'expiration_interval_unit',
        'tax_included',
    ]

    _nullables = [
        'interval_unit',
        'expiration_interval_unit',
    ]

    def __init__(self,
                 price_in_cents=None,
                 interval=None,
                 interval_unit=None,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 trial_price_in_cents=APIHelper.SKIP,
                 trial_interval=APIHelper.SKIP,
                 trial_interval_unit=APIHelper.SKIP,
                 initial_charge_in_cents=APIHelper.SKIP,
                 initial_charge_after_trial=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 tax_included=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionCustomPrice class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        price_in_cents = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionCustomPricePriceInCents'), dictionary.get('price_in_cents'), False) if dictionary.get('price_in_cents') is not None else None
        interval = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionCustomPriceInterval'), dictionary.get('interval'), False) if dictionary.get('interval') is not None else None
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else None
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        trial_price_in_cents = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionCustomPriceTrialPriceInCents'), dictionary.get('trial_price_in_cents'), False) if dictionary.get('trial_price_in_cents') is not None else APIHelper.SKIP
        trial_interval = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionCustomPriceTrialInterval'), dictionary.get('trial_interval'), False) if dictionary.get('trial_interval') is not None else APIHelper.SKIP
        trial_interval_unit = dictionary.get("trial_interval_unit") if dictionary.get("trial_interval_unit") else APIHelper.SKIP
        initial_charge_in_cents = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionCustomPriceInitialChargeInCents'), dictionary.get('initial_charge_in_cents'), False) if dictionary.get('initial_charge_in_cents') is not None else APIHelper.SKIP
        initial_charge_after_trial = dictionary.get("initial_charge_after_trial") if "initial_charge_after_trial" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionCustomPriceExpirationInterval'), dictionary.get('expiration_interval'), False) if dictionary.get('expiration_interval') is not None else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if "expiration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(price_in_cents,
                   interval,
                   interval_unit,
                   name,
                   handle,
                   trial_price_in_cents,
                   trial_interval,
                   trial_interval_unit,
                   initial_charge_in_cents,
                   initial_charge_after_trial,
                   expiration_interval,
                   expiration_interval_unit,
                   tax_included,
                   additional_properties)

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('SubscriptionCustomPricePriceInCents').validate(dictionary.price_in_cents).is_valid \
                and UnionTypeLookUp.get('SubscriptionCustomPriceInterval').validate(dictionary.interval).is_valid \
                and APIHelper.is_valid_type(value=dictionary.interval_unit,
                                            type_callable=lambda value: IntervalUnit.validate(value),
                                            is_value_nullable=True)

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('SubscriptionCustomPricePriceInCents').validate(dictionary.get('price_in_cents')).is_valid \
            and UnionTypeLookUp.get('SubscriptionCustomPriceInterval').validate(dictionary.get('interval')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('interval_unit'),
                                        type_callable=lambda value: IntervalUnit.validate(value),
                                        is_value_nullable=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!r}, '
                f'price_in_cents={self.price_in_cents!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'trial_price_in_cents={(self.trial_price_in_cents if hasattr(self, "trial_price_in_cents") else None)!r}, '
                f'trial_interval={(self.trial_interval if hasattr(self, "trial_interval") else None)!r}, '
                f'trial_interval_unit={(self.trial_interval_unit if hasattr(self, "trial_interval_unit") else None)!r}, '
                f'initial_charge_in_cents={(self.initial_charge_in_cents if hasattr(self, "initial_charge_in_cents") else None)!r}, '
                f'initial_charge_after_trial={(self.initial_charge_after_trial if hasattr(self, "initial_charge_after_trial") else None)!r}, '
                f'expiration_interval={(self.expiration_interval if hasattr(self, "expiration_interval") else None)!r}, '
                f'expiration_interval_unit={(self.expiration_interval_unit if hasattr(self, "expiration_interval_unit") else None)!r}, '
                f'tax_included={(self.tax_included if hasattr(self, "tax_included") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!s}, '
                f'price_in_cents={self.price_in_cents!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'trial_price_in_cents={(self.trial_price_in_cents if hasattr(self, "trial_price_in_cents") else None)!s}, '
                f'trial_interval={(self.trial_interval if hasattr(self, "trial_interval") else None)!s}, '
                f'trial_interval_unit={(self.trial_interval_unit if hasattr(self, "trial_interval_unit") else None)!s}, '
                f'initial_charge_in_cents={(self.initial_charge_in_cents if hasattr(self, "initial_charge_in_cents") else None)!s}, '
                f'initial_charge_after_trial={(self.initial_charge_after_trial if hasattr(self, "initial_charge_after_trial") else None)!s}, '
                f'expiration_interval={(self.expiration_interval if hasattr(self, "expiration_interval") else None)!s}, '
                f'expiration_interval_unit={(self.expiration_interval_unit if hasattr(self, "expiration_interval_unit") else None)!s}, '
                f'tax_included={(self.tax_included if hasattr(self, "tax_included") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
