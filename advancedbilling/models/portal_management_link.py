# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PortalManagementLink(object):

    """Implementation of the 'Portal Management Link' model.

    TODO: type model description here.

    Attributes:
        url (str): TODO: type description here.
        fetch_count (int): TODO: type description here.
        created_at (str): TODO: type description here.
        new_link_available_at (str): TODO: type description here.
        expires_at (str): TODO: type description here.
        last_invite_sent_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "fetch_count": 'fetch_count',
        "created_at": 'created_at',
        "new_link_available_at": 'new_link_available_at',
        "expires_at": 'expires_at',
        "last_invite_sent_at": 'last_invite_sent_at'
    }

    _optionals = [
        'url',
        'fetch_count',
        'created_at',
        'new_link_available_at',
        'expires_at',
        'last_invite_sent_at',
    ]

    _nullables = [
        'last_invite_sent_at',
    ]

    def __init__(self,
                 url=APIHelper.SKIP,
                 fetch_count=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 new_link_available_at=APIHelper.SKIP,
                 expires_at=APIHelper.SKIP,
                 last_invite_sent_at=APIHelper.SKIP):
        """Constructor for the PortalManagementLink class"""

        # Initialize members of the class
        if url is not APIHelper.SKIP:
            self.url = url 
        if fetch_count is not APIHelper.SKIP:
            self.fetch_count = fetch_count 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if new_link_available_at is not APIHelper.SKIP:
            self.new_link_available_at = new_link_available_at 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = expires_at 
        if last_invite_sent_at is not APIHelper.SKIP:
            self.last_invite_sent_at = last_invite_sent_at 

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
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        fetch_count = dictionary.get("fetch_count") if dictionary.get("fetch_count") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        new_link_available_at = dictionary.get("new_link_available_at") if dictionary.get("new_link_available_at") else APIHelper.SKIP
        expires_at = dictionary.get("expires_at") if dictionary.get("expires_at") else APIHelper.SKIP
        last_invite_sent_at = dictionary.get("last_invite_sent_at") if "last_invite_sent_at" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(url,
                   fetch_count,
                   created_at,
                   new_link_available_at,
                   expires_at,
                   last_invite_sent_at)
