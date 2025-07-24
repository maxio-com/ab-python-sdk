# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SiteStatistics(object):

    """Implementation of the 'Site Statistics' model.

    Attributes:
        total_subscriptions (int): The model property of type int.
        subscriptions_today (int): The model property of type int.
        total_revenue (str): The model property of type str.
        revenue_today (str): The model property of type str.
        revenue_this_month (str): The model property of type str.
        revenue_this_year (str): The model property of type str.
        total_canceled_subscriptions (int): The model property of type int.
        total_active_subscriptions (int): The model property of type int.
        total_past_due_subscriptions (int): The model property of type int.
        total_unpaid_subscriptions (int): The model property of type int.
        total_dunning_subscriptions (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 total_dunning_subscriptions=APIHelper.SKIP,
                 additional_properties=None):
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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   total_dunning_subscriptions,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'total_subscriptions={(self.total_subscriptions if hasattr(self, "total_subscriptions") else None)!r}, '
                f'subscriptions_today={(self.subscriptions_today if hasattr(self, "subscriptions_today") else None)!r}, '
                f'total_revenue={(self.total_revenue if hasattr(self, "total_revenue") else None)!r}, '
                f'revenue_today={(self.revenue_today if hasattr(self, "revenue_today") else None)!r}, '
                f'revenue_this_month={(self.revenue_this_month if hasattr(self, "revenue_this_month") else None)!r}, '
                f'revenue_this_year={(self.revenue_this_year if hasattr(self, "revenue_this_year") else None)!r}, '
                f'total_canceled_subscriptions={(self.total_canceled_subscriptions if hasattr(self, "total_canceled_subscriptions") else None)!r}, '
                f'total_active_subscriptions={(self.total_active_subscriptions if hasattr(self, "total_active_subscriptions") else None)!r}, '
                f'total_past_due_subscriptions={(self.total_past_due_subscriptions if hasattr(self, "total_past_due_subscriptions") else None)!r}, '
                f'total_unpaid_subscriptions={(self.total_unpaid_subscriptions if hasattr(self, "total_unpaid_subscriptions") else None)!r}, '
                f'total_dunning_subscriptions={(self.total_dunning_subscriptions if hasattr(self, "total_dunning_subscriptions") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'total_subscriptions={(self.total_subscriptions if hasattr(self, "total_subscriptions") else None)!s}, '
                f'subscriptions_today={(self.subscriptions_today if hasattr(self, "subscriptions_today") else None)!s}, '
                f'total_revenue={(self.total_revenue if hasattr(self, "total_revenue") else None)!s}, '
                f'revenue_today={(self.revenue_today if hasattr(self, "revenue_today") else None)!s}, '
                f'revenue_this_month={(self.revenue_this_month if hasattr(self, "revenue_this_month") else None)!s}, '
                f'revenue_this_year={(self.revenue_this_year if hasattr(self, "revenue_this_year") else None)!s}, '
                f'total_canceled_subscriptions={(self.total_canceled_subscriptions if hasattr(self, "total_canceled_subscriptions") else None)!s}, '
                f'total_active_subscriptions={(self.total_active_subscriptions if hasattr(self, "total_active_subscriptions") else None)!s}, '
                f'total_past_due_subscriptions={(self.total_past_due_subscriptions if hasattr(self, "total_past_due_subscriptions") else None)!s}, '
                f'total_unpaid_subscriptions={(self.total_unpaid_subscriptions if hasattr(self, "total_unpaid_subscriptions") else None)!s}, '
                f'total_dunning_subscriptions={(self.total_dunning_subscriptions if hasattr(self, "total_dunning_subscriptions") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
