# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PortalManagementLink(object):

    """Implementation of the 'Portal Management Link' model.

    Attributes:
        url (str): The model property of type str.
        fetch_count (int): The model property of type int.
        created_at (datetime): The model property of type datetime.
        new_link_available_at (datetime): The model property of type datetime.
        expires_at (datetime): The model property of type datetime.
        last_invite_sent_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 last_invite_sent_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PortalManagementLink class"""

        # Initialize members of the class
        if url is not APIHelper.SKIP:
            self.url = url 
        if fetch_count is not APIHelper.SKIP:
            self.fetch_count = fetch_count 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if new_link_available_at is not APIHelper.SKIP:
            self.new_link_available_at = APIHelper.apply_datetime_converter(new_link_available_at, APIHelper.RFC3339DateTime) if new_link_available_at else None 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
        if last_invite_sent_at is not APIHelper.SKIP:
            self.last_invite_sent_at = APIHelper.apply_datetime_converter(last_invite_sent_at, APIHelper.RFC3339DateTime) if last_invite_sent_at else None 

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
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        fetch_count = dictionary.get("fetch_count") if dictionary.get("fetch_count") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        new_link_available_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("new_link_available_at")).datetime if dictionary.get("new_link_available_at") else APIHelper.SKIP
        expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else APIHelper.SKIP
        if 'last_invite_sent_at' in dictionary.keys():
            last_invite_sent_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("last_invite_sent_at")).datetime if dictionary.get("last_invite_sent_at") else None
        else:
            last_invite_sent_at = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(url,
                   fetch_count,
                   created_at,
                   new_link_available_at,
                   expires_at,
                   last_invite_sent_at,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'url={self.url!r}, '
                f'fetch_count={self.fetch_count!r}, '
                f'created_at={self.created_at!r}, '
                f'new_link_available_at={self.new_link_available_at!r}, '
                f'expires_at={self.expires_at!r}, '
                f'last_invite_sent_at={self.last_invite_sent_at!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'url={self.url!s}, '
                f'fetch_count={self.fetch_count!s}, '
                f'created_at={self.created_at!s}, '
                f'new_link_available_at={self.new_link_available_at!s}, '
                f'expires_at={self.expires_at!s}, '
                f'last_invite_sent_at={self.last_invite_sent_at!s}, '
                f'additional_properties={self.additional_properties!s})')
