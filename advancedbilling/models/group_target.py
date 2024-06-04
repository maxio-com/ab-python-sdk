# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.group_target_type import GroupTargetType


class GroupTarget(object):

    """Implementation of the 'Group Target' model.

    Attributes of the target customer who will be the responsible payer of the
    created subscription. Required.

    Attributes:
        mtype (GroupTargetType): The type of object indicated by the id
            attribute.
        id (int): The id of the target customer or subscription to group the
            existing subscription with. Ignored and should not be included if
            type is "self" , "parent", or "eldest"

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "id": 'id'
    }

    _optionals = [
        'id',
    ]

    def __init__(self,
                 mtype=None,
                 id=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the GroupTarget class"""

        # Initialize members of the class
        self.mtype = mtype 
        if id is not APIHelper.SKIP:
            self.id = id 

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
        mtype = dictionary.get("type") if dictionary.get("type") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(mtype,
                   id,
                   dictionary)

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

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.mtype,
                                           type_callable=lambda value: GroupTargetType.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('type'),
                                       type_callable=lambda value: GroupTargetType.validate(value))
