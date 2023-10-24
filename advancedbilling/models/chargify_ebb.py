# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ChargifyEBB(object):

    """Implementation of the 'Chargify EBB' model.

    TODO: type model description here.

    Attributes:
        timestamp (str): This timestamp determines what billing period the
            event will be billed in. If your request payload does not include
            it, Chargify will add `chargify.timestamp` to the event payload
            and set the value to `now`.
        id (str): A unique ID set by Chargify. Please note that this field is
            reserved. If `chargify.id` is present in the request payload, it
            will be overwritten.
        created_at (str): An ISO-8601 timestamp, set by Chargify at the time
            each event is recorded. Please note that this field is reserved.
            If `chargify.created_at` is present in the request payload, it
            will be overwritten.
        uniqueness_token (str): User-defined string scoped per-stream.
            Duplicate events within a stream will be silently ignored. Tokens
            expire after 31 days.
        subscription_id (int): Id of Maxio Advanced Billing Subscription which
            is connected to this event.  Provide `subscription_id` if you
            configured `chargify.subscription_id` as Subscription Identifier
            in your Event Stream.
        subscription_reference (str): Reference of Maxio Advanced Billing
            Subscription which is connected to this event.  Provide
            `subscription_reference` if you configured
            `chargify.subscription_reference` as Subscription Identifier in
            your Event Stream.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp": 'timestamp',
        "id": 'id',
        "created_at": 'created_at',
        "uniqueness_token": 'uniqueness_token',
        "subscription_id": 'subscription_id',
        "subscription_reference": 'subscription_reference'
    }

    _optionals = [
        'timestamp',
        'id',
        'created_at',
        'uniqueness_token',
        'subscription_id',
        'subscription_reference',
    ]

    def __init__(self,
                 timestamp=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 uniqueness_token=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 subscription_reference=APIHelper.SKIP):
        """Constructor for the ChargifyEBB class"""

        # Initialize members of the class
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 
        if id is not APIHelper.SKIP:
            self.id = id 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if uniqueness_token is not APIHelper.SKIP:
            self.uniqueness_token = uniqueness_token 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if subscription_reference is not APIHelper.SKIP:
            self.subscription_reference = subscription_reference 

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
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        uniqueness_token = dictionary.get("uniqueness_token") if dictionary.get("uniqueness_token") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        subscription_reference = dictionary.get("subscription_reference") if dictionary.get("subscription_reference") else APIHelper.SKIP
        # Return an object of this model
        return cls(timestamp,
                   id,
                   created_at,
                   uniqueness_token,
                   subscription_id,
                   subscription_reference)
