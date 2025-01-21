# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RevokedInvitation(object):

    """Implementation of the 'Revoked Invitation' model.

    Attributes:
        last_sent_at (str): The model property of type str.
        last_accepted_at (str): The model property of type str.
        uninvited_count (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_sent_at": 'last_sent_at',
        "last_accepted_at": 'last_accepted_at',
        "uninvited_count": 'uninvited_count'
    }

    _optionals = [
        'last_sent_at',
        'last_accepted_at',
        'uninvited_count',
    ]

    def __init__(self,
                 last_sent_at=APIHelper.SKIP,
                 last_accepted_at=APIHelper.SKIP,
                 uninvited_count=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RevokedInvitation class"""

        # Initialize members of the class
        if last_sent_at is not APIHelper.SKIP:
            self.last_sent_at = last_sent_at 
        if last_accepted_at is not APIHelper.SKIP:
            self.last_accepted_at = last_accepted_at 
        if uninvited_count is not APIHelper.SKIP:
            self.uninvited_count = uninvited_count 

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
        uninvited_count = dictionary.get("uninvited_count") if dictionary.get("uninvited_count") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(last_sent_at,
                   last_accepted_at,
                   uninvited_count,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'last_sent_at={self.last_sent_at!r}, '
                f'last_accepted_at={self.last_accepted_at!r}, '
                f'uninvited_count={self.uninvited_count!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'last_sent_at={self.last_sent_at!s}, '
                f'last_accepted_at={self.last_accepted_at!s}, '
                f'uninvited_count={self.uninvited_count!s}, '
                f'additional_properties={self.additional_properties!s})')
