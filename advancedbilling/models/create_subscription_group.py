# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateSubscriptionGroup(object):

    """Implementation of the 'Create Subscription Group' model.

    Attributes:
        subscription_id (int): The model property of type int.
        member_ids (List[int]): The model property of type List[int].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": 'subscription_id',
        "member_ids": 'member_ids'
    }

    _optionals = [
        'member_ids',
    ]

    def __init__(self,
                 subscription_id=None,
                 member_ids=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateSubscriptionGroup class"""

        # Initialize members of the class
        self.subscription_id = subscription_id 
        if member_ids is not APIHelper.SKIP:
            self.member_ids = member_ids 

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
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        member_ids = dictionary.get("member_ids") if dictionary.get("member_ids") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscription_id,
                   member_ids,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_id={self.subscription_id!r}, '
                f'member_ids={(self.member_ids if hasattr(self, "member_ids") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_id={self.subscription_id!s}, '
                f'member_ids={(self.member_ids if hasattr(self, "member_ids") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
