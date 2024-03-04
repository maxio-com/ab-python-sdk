# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Endpoint(object):

    """Implementation of the 'Endpoint' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        url (str): TODO: type description here.
        site_id (int): TODO: type description here.
        status (str): TODO: type description here.
        webhook_subscriptions (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "url": 'url',
        "site_id": 'site_id',
        "status": 'status',
        "webhook_subscriptions": 'webhook_subscriptions'
    }

    _optionals = [
        'id',
        'url',
        'site_id',
        'status',
        'webhook_subscriptions',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 webhook_subscriptions=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the Endpoint class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if url is not APIHelper.SKIP:
            self.url = url 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if webhook_subscriptions is not APIHelper.SKIP:
            self.webhook_subscriptions = webhook_subscriptions 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        webhook_subscriptions = dictionary.get("webhook_subscriptions") if dictionary.get("webhook_subscriptions") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   url,
                   site_id,
                   status,
                   webhook_subscriptions,
                   dictionary)
