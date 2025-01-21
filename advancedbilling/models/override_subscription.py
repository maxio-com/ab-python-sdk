# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class OverrideSubscription(object):

    """Implementation of the 'Override Subscription' model.

    Attributes:
        activated_at (datetime): Can be used to record an external signup
            date. Chargify uses this field to record when a subscription first
            goes active (either at signup or at trial end). Only ISO8601
            format is supported.
        canceled_at (datetime): Can be used to record an external cancellation
            date. Chargify sets this field automatically when a subscription
            is canceled, whether by request or via dunning. Only ISO8601
            format is supported.
        cancellation_message (str): Can be used to record a reason for the
            original cancellation.
        expires_at (datetime): Can be used to record an external expiration
            date. Chargify sets this field automatically when a subscription
            expires (ceases billing) after a prescribed amount of time. Only
            ISO8601 format is supported.
        current_period_starts_at (datetime): Can only be used when a
            subscription is unbilled, which happens when a future initial
            billing date is passed at subscription creation. The value passed
            must be before the current date and time. Allows you to set when
            the period started so mid period component allocations have the
            correct proration. Only ISO8601 format is supported.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "activated_at": 'activated_at',
        "canceled_at": 'canceled_at',
        "cancellation_message": 'cancellation_message',
        "expires_at": 'expires_at',
        "current_period_starts_at": 'current_period_starts_at'
    }

    _optionals = [
        'activated_at',
        'canceled_at',
        'cancellation_message',
        'expires_at',
        'current_period_starts_at',
    ]

    def __init__(self,
                 activated_at=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 cancellation_message=APIHelper.SKIP,
                 expires_at=APIHelper.SKIP,
                 current_period_starts_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OverrideSubscription class"""

        # Initialize members of the class
        if activated_at is not APIHelper.SKIP:
            self.activated_at = APIHelper.apply_datetime_converter(activated_at, APIHelper.RFC3339DateTime) if activated_at else None 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = APIHelper.apply_datetime_converter(canceled_at, APIHelper.RFC3339DateTime) if canceled_at else None 
        if cancellation_message is not APIHelper.SKIP:
            self.cancellation_message = cancellation_message 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
        if current_period_starts_at is not APIHelper.SKIP:
            self.current_period_starts_at = APIHelper.apply_datetime_converter(current_period_starts_at, APIHelper.RFC3339DateTime) if current_period_starts_at else None 

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
        activated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("activated_at")).datetime if dictionary.get("activated_at") else APIHelper.SKIP
        canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else APIHelper.SKIP
        cancellation_message = dictionary.get("cancellation_message") if dictionary.get("cancellation_message") else APIHelper.SKIP
        expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else APIHelper.SKIP
        current_period_starts_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("current_period_starts_at")).datetime if dictionary.get("current_period_starts_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(activated_at,
                   canceled_at,
                   cancellation_message,
                   expires_at,
                   current_period_starts_at,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'activated_at={self.activated_at!r}, '
                f'canceled_at={self.canceled_at!r}, '
                f'cancellation_message={self.cancellation_message!r}, '
                f'expires_at={self.expires_at!r}, '
                f'current_period_starts_at={self.current_period_starts_at!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'activated_at={self.activated_at!s}, '
                f'canceled_at={self.canceled_at!s}, '
                f'cancellation_message={self.cancellation_message!s}, '
                f'expires_at={self.expires_at!s}, '
                f'current_period_starts_at={self.current_period_starts_at!s}, '
                f'additional_properties={self.additional_properties!s})')
