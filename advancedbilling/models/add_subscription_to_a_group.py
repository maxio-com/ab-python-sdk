# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AddSubscriptionToAGroup(object):

    """Implementation of the 'Add Subscription to a Group' model.

    TODO: type model description here.

    Attributes:
        group (GroupSettings | bool | None): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group": 'group'
    }

    _optionals = [
        'group',
    ]

    def __init__(self,
                 group=APIHelper.SKIP):
        """Constructor for the AddSubscriptionToAGroup class"""

        # Initialize members of the class
        if group is not APIHelper.SKIP:
            self.group = group 

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
        group = APIHelper.deserialize_union_type(UnionTypeLookUp.get('AddSubscriptionToAGroupGroup'), dictionary.get('group'), False) if dictionary.get('group') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(group)
