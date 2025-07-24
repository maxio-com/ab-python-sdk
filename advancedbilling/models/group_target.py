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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the GroupTarget class"""

        # Initialize members of the class
        self.mtype = mtype 
        if id is not APIHelper.SKIP:
            self.id = id 

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
        mtype = dictionary.get("type") if dictionary.get("type") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(mtype,
                   id,
                   additional_properties)

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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!r}, '
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!s}, '
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
