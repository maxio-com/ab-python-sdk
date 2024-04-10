# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_filter import SubscriptionFilter


class ListSubscriptionComponentsForSiteFilter(object):

    """Implementation of the 'List Subscription Components For Site Filter' model.

    TODO: type model description here.

    Attributes:
        currencies (List[str]): Allows fetching components allocation with
            matching currency based on provided values. Use in query
            `filter[currencies]=USD,EUR`.
        use_site_exchange_rate (bool): Allows fetching components allocation
            with matching use_site_exchange_rate based on provided value. Use
            in query `filter[use_site_exchange_rate]=true`.
        subscription (SubscriptionFilter): Nested filter used for List
            Subscription Components For Site Filter

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currencies": 'currencies',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "subscription": 'subscription'
    }

    _optionals = [
        'currencies',
        'use_site_exchange_rate',
        'subscription',
    ]

    def __init__(self,
                 currencies=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 subscription=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListSubscriptionComponentsForSiteFilter class"""

        # Initialize members of the class
        if currencies is not APIHelper.SKIP:
            self.currencies = currencies 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 

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
        currencies = dictionary.get("currencies") if dictionary.get("currencies") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        subscription = SubscriptionFilter.from_dictionary(dictionary.get('subscription')) if 'subscription' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(currencies,
                   use_site_exchange_rate,
                   subscription,
                   dictionary)
