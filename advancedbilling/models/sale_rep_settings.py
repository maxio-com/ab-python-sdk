# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SaleRepSettings(object):

    """Implementation of the 'Sale Rep Settings' model.

    TODO: type model description here.

    Attributes:
        customer_name (str): TODO: type description here.
        subscription_id (int): TODO: type description here.
        site_link (str): TODO: type description here.
        site_name (str): TODO: type description here.
        subscription_mrr (str): TODO: type description here.
        sales_rep_id (int): TODO: type description here.
        sales_rep_name (str): TODO: type description here.

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
                 sales_rep_name=APIHelper.SKIP):
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
        customer_name = dictionary.get("customer_name") if dictionary.get("customer_name") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        site_link = dictionary.get("site_link") if dictionary.get("site_link") else APIHelper.SKIP
        site_name = dictionary.get("site_name") if dictionary.get("site_name") else APIHelper.SKIP
        subscription_mrr = dictionary.get("subscription_mrr") if dictionary.get("subscription_mrr") else APIHelper.SKIP
        sales_rep_id = dictionary.get("sales_rep_id") if dictionary.get("sales_rep_id") else APIHelper.SKIP
        sales_rep_name = dictionary.get("sales_rep_name") if dictionary.get("sales_rep_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer_name,
                   subscription_id,
                   site_link,
                   site_name,
                   subscription_mrr,
                   sales_rep_id,
                   sales_rep_name)
