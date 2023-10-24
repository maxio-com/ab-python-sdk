# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReferralCode(object):

    """Implementation of the 'Referral Code' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        site_id (int): TODO: type description here.
        subscription_id (int): TODO: type description here.
        code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "site_id": 'site_id',
        "subscription_id": 'subscription_id',
        "code": 'code'
    }

    _optionals = [
        'id',
        'site_id',
        'subscription_id',
        'code',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 code=APIHelper.SKIP):
        """Constructor for the ReferralCode class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if code is not APIHelper.SKIP:
            self.code = code 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   site_id,
                   subscription_id,
                   code)
