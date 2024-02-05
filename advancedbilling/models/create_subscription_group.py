# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateSubscriptionGroup(object):

    """Implementation of the 'Create Subscription Group' model.

    TODO: type model description here.

    Attributes:
        subscription_id (str | int): TODO: type description here.
        member_ids (List[int]): TODO: type description here.

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
                 member_ids=APIHelper.SKIP):
        """Constructor for the CreateSubscriptionGroup class"""

        # Initialize members of the class
        self.subscription_id = subscription_id 
        if member_ids is not APIHelper.SKIP:
            self.member_ids = member_ids 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        subscription_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionGroupSubscriptionId'), dictionary.get('subscription_id'), False) if dictionary.get('subscription_id') is not None else None
        member_ids = dictionary.get("member_ids") if dictionary.get("member_ids") else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription_id,
                   member_ids)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('CreateSubscriptionGroupSubscriptionId').validate(dictionary.subscription_id).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('CreateSubscriptionGroupSubscriptionId').validate(dictionary.get('subscription_id')).is_valid
