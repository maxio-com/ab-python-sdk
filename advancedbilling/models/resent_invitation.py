# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ResentInvitation(object):

    """Implementation of the 'Resent Invitation' model.

    TODO: type model description here.

    Attributes:
        last_sent_at (str): TODO: type description here.
        last_accepted_at (str): TODO: type description here.
        send_invite_link_text (str): TODO: type description here.
        uninvited_count (int): TODO: type description here.
        last_invite_sent_at (datetime): TODO: type description here.
        last_invite_accepted_at (datetime): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_sent_at": 'last_sent_at',
        "last_accepted_at": 'last_accepted_at',
        "send_invite_link_text": 'send_invite_link_text',
        "uninvited_count": 'uninvited_count',
        "last_invite_sent_at": 'last_invite_sent_at',
        "last_invite_accepted_at": 'last_invite_accepted_at'
    }

    _optionals = [
        'last_sent_at',
        'last_accepted_at',
        'send_invite_link_text',
        'uninvited_count',
        'last_invite_sent_at',
        'last_invite_accepted_at',
    ]

    def __init__(self,
                 last_sent_at=APIHelper.SKIP,
                 last_accepted_at=APIHelper.SKIP,
                 send_invite_link_text=APIHelper.SKIP,
                 uninvited_count=APIHelper.SKIP,
                 last_invite_sent_at=APIHelper.SKIP,
                 last_invite_accepted_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ResentInvitation class"""

        # Initialize members of the class
        if last_sent_at is not APIHelper.SKIP:
            self.last_sent_at = last_sent_at 
        if last_accepted_at is not APIHelper.SKIP:
            self.last_accepted_at = last_accepted_at 
        if send_invite_link_text is not APIHelper.SKIP:
            self.send_invite_link_text = send_invite_link_text 
        if uninvited_count is not APIHelper.SKIP:
            self.uninvited_count = uninvited_count 
        if last_invite_sent_at is not APIHelper.SKIP:
            self.last_invite_sent_at = APIHelper.apply_datetime_converter(last_invite_sent_at, APIHelper.RFC3339DateTime) if last_invite_sent_at else None 
        if last_invite_accepted_at is not APIHelper.SKIP:
            self.last_invite_accepted_at = APIHelper.apply_datetime_converter(last_invite_accepted_at, APIHelper.RFC3339DateTime) if last_invite_accepted_at else None 

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
        last_sent_at = dictionary.get("last_sent_at") if dictionary.get("last_sent_at") else APIHelper.SKIP
        last_accepted_at = dictionary.get("last_accepted_at") if dictionary.get("last_accepted_at") else APIHelper.SKIP
        send_invite_link_text = dictionary.get("send_invite_link_text") if dictionary.get("send_invite_link_text") else APIHelper.SKIP
        uninvited_count = dictionary.get("uninvited_count") if dictionary.get("uninvited_count") else APIHelper.SKIP
        last_invite_sent_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("last_invite_sent_at")).datetime if dictionary.get("last_invite_sent_at") else APIHelper.SKIP
        last_invite_accepted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("last_invite_accepted_at")).datetime if dictionary.get("last_invite_accepted_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(last_sent_at,
                   last_accepted_at,
                   send_invite_link_text,
                   uninvited_count,
                   last_invite_sent_at,
                   last_invite_accepted_at,
                   additional_properties)
