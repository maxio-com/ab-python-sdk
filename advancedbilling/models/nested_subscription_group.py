# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class NestedSubscriptionGroup(object):

    """Implementation of the 'Nested Subscription Group' model.

    Attributes:
        uid (str): The UID for the group
        scheme (int): Whether the group is configured to rely on a primary
            subscription for billing. At this time, it will always be 1.
        primary_subscription_id (int): The subscription ID of the primary
            within the group. Applicable to scheme 1.
        primary (bool): A boolean indicating whether the subscription is the
            primary in the group. Applicable to scheme 1.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else APIHelper.SKIP
        primary_subscription_id = dictionary.get("primary_subscription_id") if dictionary.get("primary_subscription_id") else APIHelper.SKIP
        primary = dictionary.get("primary") if "primary" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   scheme,
                   primary_subscription_id,
                   primary,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'scheme={(self.scheme if hasattr(self, "scheme") else None)!r}, '
                f'primary_subscription_id={(self.primary_subscription_id if hasattr(self, "primary_subscription_id") else None)!r}, '
                f'primary={(self.primary if hasattr(self, "primary") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'scheme={(self.scheme if hasattr(self, "scheme") else None)!s}, '
                f'primary_subscription_id={(self.primary_subscription_id if hasattr(self, "primary_subscription_id") else None)!s}, '
                f'primary={(self.primary if hasattr(self, "primary") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
