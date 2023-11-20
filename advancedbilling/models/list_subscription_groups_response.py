# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.list_subscription_groups_item import ListSubscriptionGroupsItem
from advancedbilling.models.list_subscription_groups_meta import ListSubscriptionGroupsMeta


class ListSubscriptionGroupsResponse(object):

    """Implementation of the 'List Subscription Groups Response' model.

    TODO: type model description here.

    Attributes:
        subscription_groups (List[ListSubscriptionGroupsItem]): TODO: type
            description here.
        meta (ListSubscriptionGroupsMeta): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_groups": 'subscription_groups',
        "meta": 'meta'
    }

    _optionals = [
        'subscription_groups',
        'meta',
    ]

    def __init__(self,
                 subscription_groups=APIHelper.SKIP,
                 meta=APIHelper.SKIP):
        """Constructor for the ListSubscriptionGroupsResponse class"""

        # Initialize members of the class
        if subscription_groups is not APIHelper.SKIP:
            self.subscription_groups = subscription_groups 
        if meta is not APIHelper.SKIP:
            self.meta = meta 

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
        subscription_groups = None
        if dictionary.get('subscription_groups') is not None:
            subscription_groups = [ListSubscriptionGroupsItem.from_dictionary(x) for x in dictionary.get('subscription_groups')]
        else:
            subscription_groups = APIHelper.SKIP
        meta = ListSubscriptionGroupsMeta.from_dictionary(dictionary.get('meta')) if 'meta' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription_groups,
                   meta)
