# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class NestedSubscriptionGroup(object):

    """Implementation of the 'Nested Subscription Group' model.

    TODO: type model description here.

    Attributes:
        uid (str): The UID for the group
        scheme (int): Whether the group is configured to rely on a primary
            subscription for billing. At this time, it will always be 1.
        primary_subscription_id (int): The subscription ID of the primary
            within the group. Applicable to scheme 1.
        primary (bool): A boolean indicating whether the subscription is the
            primary in the group. Applicable to scheme 1.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "scheme": 'scheme',
        "primary_subscription_id": 'primary_subscription_id',
        "primary": 'primary'
    }

    _optionals = [
        'uid',
        'scheme',
        'primary_subscription_id',
        'primary',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 scheme=APIHelper.SKIP,
                 primary_subscription_id=APIHelper.SKIP,
                 primary=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the NestedSubscriptionGroup class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if scheme is not APIHelper.SKIP:
            self.scheme = scheme 
        if primary_subscription_id is not APIHelper.SKIP:
            self.primary_subscription_id = primary_subscription_id 
        if primary is not APIHelper.SKIP:
            self.primary = primary 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else APIHelper.SKIP
        primary_subscription_id = dictionary.get("primary_subscription_id") if dictionary.get("primary_subscription_id") else APIHelper.SKIP
        primary = dictionary.get("primary") if "primary" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(uid,
                   scheme,
                   primary_subscription_id,
                   primary,
                   dictionary)
