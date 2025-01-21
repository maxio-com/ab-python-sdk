# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DeleteSubscriptionGroupResponse(object):

    """Implementation of the 'Delete Subscription Group Response' model.

    Attributes:
        uid (str): The model property of type str.
        deleted (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "deleted": 'deleted'
    }

    _optionals = [
        'uid',
        'deleted',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 deleted=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the DeleteSubscriptionGroupResponse class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        deleted = dictionary.get("deleted") if "deleted" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   deleted,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!r}, '
                f'deleted={self.deleted!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!s}, '
                f'deleted={self.deleted!s}, '
                f'additional_properties={self.additional_properties!s})')
