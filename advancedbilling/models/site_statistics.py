# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SiteStatistics(object):

    """Implementation of the 'Site Statistics' model.

    TODO: type model description here.

    Attributes:
        total_subscriptions (int): TODO: type description here.
        subscriptions_today (int): TODO: type description here.
        total_revenue (str): TODO: type description here.
        revenue_today (str): TODO: type description here.
        revenue_this_month (str): TODO: type description here.
        revenue_this_year (str): TODO: type description here.
        total_canceled_subscriptions (int): TODO: type description here.
        total_active_subscriptions (float): TODO: type description here.
        total_past_due_subscriptions (float): TODO: type description here.
        total_unpaid_subscriptions (float): TODO: type description here.
        total_dunning_subscriptions (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_subscriptions": 'total_subscriptions',
        "subscriptions_today": 'subscriptions_today',
        "total_revenue": 'total_revenue',
        "revenue_today": 'revenue_today',
        "revenue_this_month": 'revenue_this_month',
        "revenue_this_year": 'revenue_this_year',
        "total_canceled_subscriptions": 'total_canceled_subscriptions',
        "total_active_subscriptions": 'total_active_subscriptions',
        "total_past_due_subscriptions": 'total_past_due_subscriptions',
        "total_unpaid_subscriptions": 'total_unpaid_subscriptions',
        "total_dunning_subscriptions": 'total_dunning_subscriptions'
    }

    _optionals = [
        'total_subscriptions',
        'subscriptions_today',
        'total_revenue',
        'revenue_today',
        'revenue_this_month',
        'revenue_this_year',
        'total_canceled_subscriptions',
        'total_active_subscriptions',
        'total_past_due_subscriptions',
        'total_unpaid_subscriptions',
        'total_dunning_subscriptions',
    ]

    def __init__(self,
                 total_subscriptions=APIHelper.SKIP,
                 subscriptions_today=APIHelper.SKIP,
                 total_revenue=APIHelper.SKIP,
                 revenue_today=APIHelper.SKIP,
                 revenue_this_month=APIHelper.SKIP,
                 revenue_this_year=APIHelper.SKIP,
                 total_canceled_subscriptions=APIHelper.SKIP,
                 total_active_subscriptions=APIHelper.SKIP,
                 total_past_due_subscriptions=APIHelper.SKIP,
                 total_unpaid_subscriptions=APIHelper.SKIP,
                 total_dunning_subscriptions=APIHelper.SKIP):
        """Constructor for the SiteStatistics class"""

        # Initialize members of the class
        if total_subscriptions is not APIHelper.SKIP:
            self.total_subscriptions = total_subscriptions 
        if subscriptions_today is not APIHelper.SKIP:
            self.subscriptions_today = subscriptions_today 
        if total_revenue is not APIHelper.SKIP:
            self.total_revenue = total_revenue 
        if revenue_today is not APIHelper.SKIP:
            self.revenue_today = revenue_today 
        if revenue_this_month is not APIHelper.SKIP:
            self.revenue_this_month = revenue_this_month 
        if revenue_this_year is not APIHelper.SKIP:
            self.revenue_this_year = revenue_this_year 
        if total_canceled_subscriptions is not APIHelper.SKIP:
            self.total_canceled_subscriptions = total_canceled_subscriptions 
        if total_active_subscriptions is not APIHelper.SKIP:
            self.total_active_subscriptions = total_active_subscriptions 
        if total_past_due_subscriptions is not APIHelper.SKIP:
            self.total_past_due_subscriptions = total_past_due_subscriptions 
        if total_unpaid_subscriptions is not APIHelper.SKIP:
            self.total_unpaid_subscriptions = total_unpaid_subscriptions 
        if total_dunning_subscriptions is not APIHelper.SKIP:
            self.total_dunning_subscriptions = total_dunning_subscriptions 

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
        total_subscriptions = dictionary.get("total_subscriptions") if dictionary.get("total_subscriptions") else APIHelper.SKIP
        subscriptions_today = dictionary.get("subscriptions_today") if dictionary.get("subscriptions_today") else APIHelper.SKIP
        total_revenue = dictionary.get("total_revenue") if dictionary.get("total_revenue") else APIHelper.SKIP
        revenue_today = dictionary.get("revenue_today") if dictionary.get("revenue_today") else APIHelper.SKIP
        revenue_this_month = dictionary.get("revenue_this_month") if dictionary.get("revenue_this_month") else APIHelper.SKIP
        revenue_this_year = dictionary.get("revenue_this_year") if dictionary.get("revenue_this_year") else APIHelper.SKIP
        total_canceled_subscriptions = dictionary.get("total_canceled_subscriptions") if dictionary.get("total_canceled_subscriptions") else APIHelper.SKIP
        total_active_subscriptions = dictionary.get("total_active_subscriptions") if dictionary.get("total_active_subscriptions") else APIHelper.SKIP
        total_past_due_subscriptions = dictionary.get("total_past_due_subscriptions") if dictionary.get("total_past_due_subscriptions") else APIHelper.SKIP
        total_unpaid_subscriptions = dictionary.get("total_unpaid_subscriptions") if dictionary.get("total_unpaid_subscriptions") else APIHelper.SKIP
        total_dunning_subscriptions = dictionary.get("total_dunning_subscriptions") if dictionary.get("total_dunning_subscriptions") else APIHelper.SKIP
        # Return an object of this model
        return cls(total_subscriptions,
                   subscriptions_today,
                   total_revenue,
                   revenue_today,
                   revenue_this_month,
                   revenue_this_year,
                   total_canceled_subscriptions,
                   total_active_subscriptions,
                   total_past_due_subscriptions,
                   total_unpaid_subscriptions,
                   total_dunning_subscriptions)
