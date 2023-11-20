# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class OverrideSubscription(object):

    """Implementation of the 'Override Subscription' model.

    TODO: type model description here.

    Attributes:
        activated_at (str): Can be used to record an external signup date.
            Chargify uses this field to record when a subscription first goes
            active (either at signup or at trial end)
        canceled_at (str): Can be used to record an external cancellation
            date. Chargify sets this field automatically when a subscription
            is canceled, whether by request or via dunning.
        cancellation_message (str): Can be used to record a reason for the
            original cancellation.
        expires_at (str): Can be used to record an external expiration date.
            Chargify sets this field automatically when a subscription expires
            (ceases billing) after a prescribed amount of time.
        current_period_starts_at (str): Can only be used when a subscription
            is unbilled, which happens when a future initial billing date is
            passed at subscription creation. The value passed must be before
            the current date and time. Allows you to set when the period
            started so mid period component allocations have the correct
            proration.

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
                 current_period_starts_at=APIHelper.SKIP):
        """Constructor for the OverrideSubscription class"""

        # Initialize members of the class
        if activated_at is not APIHelper.SKIP:
            self.activated_at = activated_at 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = canceled_at 
        if cancellation_message is not APIHelper.SKIP:
            self.cancellation_message = cancellation_message 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = expires_at 
        if current_period_starts_at is not APIHelper.SKIP:
            self.current_period_starts_at = current_period_starts_at 

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
        activated_at = dictionary.get("activated_at") if dictionary.get("activated_at") else APIHelper.SKIP
        canceled_at = dictionary.get("canceled_at") if dictionary.get("canceled_at") else APIHelper.SKIP
        cancellation_message = dictionary.get("cancellation_message") if dictionary.get("cancellation_message") else APIHelper.SKIP
        expires_at = dictionary.get("expires_at") if dictionary.get("expires_at") else APIHelper.SKIP
        current_period_starts_at = dictionary.get("current_period_starts_at") if dictionary.get("current_period_starts_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(activated_at,
                   canceled_at,
                   cancellation_message,
                   expires_at,
                   current_period_starts_at)
