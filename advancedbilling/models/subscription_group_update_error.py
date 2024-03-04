# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_member_error import SubscriptionGroupMemberError


class SubscriptionGroupUpdateError(object):

    """Implementation of the 'Subscription Group Update Error' model.

    TODO: type model description here.

    Attributes:
        members (List[SubscriptionGroupMemberError]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "members": 'members'
    }

    _optionals = [
        'members',
    ]

    def __init__(self,
                 members=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the SubscriptionGroupUpdateError class"""

        # Initialize members of the class
        if members is not APIHelper.SKIP:
            self.members = members 

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
        members = None
        if dictionary.get('members') is not None:
            members = [SubscriptionGroupMemberError.from_dictionary(x) for x in dictionary.get('members')]
        else:
            members = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(members,
                   dictionary)
