# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SaleRepSettings(object):

    """Implementation of the 'Sale Rep Settings' model.

    Attributes:
        customer_name (str): The model property of type str.
        subscription_id (int): The model property of type int.
        site_link (str): The model property of type str.
        site_name (str): The model property of type str.
        subscription_mrr (str): The model property of type str.
        sales_rep_id (int): The model property of type int.
        sales_rep_name (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_name": 'customer_name',
        "subscription_id": 'subscription_id',
        "site_link": 'site_link',
        "site_name": 'site_name',
        "subscription_mrr": 'subscription_mrr',
        "sales_rep_id": 'sales_rep_id',
        "sales_rep_name": 'sales_rep_name'
    }

    _optionals = [
        'customer_name',
        'subscription_id',
        'site_link',
        'site_name',
        'subscription_mrr',
        'sales_rep_id',
        'sales_rep_name',
    ]

    def __init__(self,
                 customer_name=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 site_link=APIHelper.SKIP,
                 site_name=APIHelper.SKIP,
                 subscription_mrr=APIHelper.SKIP,
                 sales_rep_id=APIHelper.SKIP,
                 sales_rep_name=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SaleRepSettings class"""

        # Initialize members of the class
        if customer_name is not APIHelper.SKIP:
            self.customer_name = customer_name 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if site_link is not APIHelper.SKIP:
            self.site_link = site_link 
        if site_name is not APIHelper.SKIP:
            self.site_name = site_name 
        if subscription_mrr is not APIHelper.SKIP:
            self.subscription_mrr = subscription_mrr 
        if sales_rep_id is not APIHelper.SKIP:
            self.sales_rep_id = sales_rep_id 
        if sales_rep_name is not APIHelper.SKIP:
            self.sales_rep_name = sales_rep_name 

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
        customer_name = dictionary.get("customer_name") if dictionary.get("customer_name") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        site_link = dictionary.get("site_link") if dictionary.get("site_link") else APIHelper.SKIP
        site_name = dictionary.get("site_name") if dictionary.get("site_name") else APIHelper.SKIP
        subscription_mrr = dictionary.get("subscription_mrr") if dictionary.get("subscription_mrr") else APIHelper.SKIP
        sales_rep_id = dictionary.get("sales_rep_id") if dictionary.get("sales_rep_id") else APIHelper.SKIP
        sales_rep_name = dictionary.get("sales_rep_name") if dictionary.get("sales_rep_name") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(customer_name,
                   subscription_id,
                   site_link,
                   site_name,
                   subscription_mrr,
                   sales_rep_id,
                   sales_rep_name,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'customer_name={(self.customer_name if hasattr(self, "customer_name") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'site_link={(self.site_link if hasattr(self, "site_link") else None)!r}, '
                f'site_name={(self.site_name if hasattr(self, "site_name") else None)!r}, '
                f'subscription_mrr={(self.subscription_mrr if hasattr(self, "subscription_mrr") else None)!r}, '
                f'sales_rep_id={(self.sales_rep_id if hasattr(self, "sales_rep_id") else None)!r}, '
                f'sales_rep_name={(self.sales_rep_name if hasattr(self, "sales_rep_name") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'customer_name={(self.customer_name if hasattr(self, "customer_name") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'site_link={(self.site_link if hasattr(self, "site_link") else None)!s}, '
                f'site_name={(self.site_name if hasattr(self, "site_name") else None)!s}, '
                f'subscription_mrr={(self.subscription_mrr if hasattr(self, "subscription_mrr") else None)!s}, '
                f'sales_rep_id={(self.sales_rep_id if hasattr(self, "sales_rep_id") else None)!s}, '
                f'sales_rep_name={(self.sales_rep_name if hasattr(self, "sales_rep_name") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
