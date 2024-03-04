# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.site_statistics import SiteStatistics


class SiteSummary(object):

    """Implementation of the 'Site Summary' model.

    TODO: type model description here.

    Attributes:
        seller_name (str): TODO: type description here.
        site_name (str): TODO: type description here.
        site_id (int): TODO: type description here.
        site_currency (str): TODO: type description here.
        stats (SiteStatistics): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "seller_name": 'seller_name',
        "site_name": 'site_name',
        "site_id": 'site_id',
        "site_currency": 'site_currency',
        "stats": 'stats'
    }

    _optionals = [
        'seller_name',
        'site_name',
        'site_id',
        'site_currency',
        'stats',
    ]

    def __init__(self,
                 seller_name=APIHelper.SKIP,
                 site_name=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 site_currency=APIHelper.SKIP,
                 stats=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the SiteSummary class"""

        # Initialize members of the class
        if seller_name is not APIHelper.SKIP:
            self.seller_name = seller_name 
        if site_name is not APIHelper.SKIP:
            self.site_name = site_name 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if site_currency is not APIHelper.SKIP:
            self.site_currency = site_currency 
        if stats is not APIHelper.SKIP:
            self.stats = stats 

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
        seller_name = dictionary.get("seller_name") if dictionary.get("seller_name") else APIHelper.SKIP
        site_name = dictionary.get("site_name") if dictionary.get("site_name") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        site_currency = dictionary.get("site_currency") if dictionary.get("site_currency") else APIHelper.SKIP
        stats = SiteStatistics.from_dictionary(dictionary.get('stats')) if 'stats' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(seller_name,
                   site_name,
                   site_id,
                   site_currency,
                   stats,
                   dictionary)
