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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 meta=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListSubscriptionGroupsResponse class"""

        # Initialize members of the class
        if subscription_groups is not APIHelper.SKIP:
            self.subscription_groups = subscription_groups 
        if meta is not APIHelper.SKIP:
            self.meta = meta 

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
        subscription_groups = None
        if dictionary.get('subscription_groups') is not None:
            subscription_groups = [ListSubscriptionGroupsItem.from_dictionary(x) for x in dictionary.get('subscription_groups')]
        else:
            subscription_groups = APIHelper.SKIP
        meta = ListSubscriptionGroupsMeta.from_dictionary(dictionary.get('meta')) if 'meta' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscription_groups,
                   meta,
                   additional_properties)
