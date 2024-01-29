# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReasonCode(object):

    """Implementation of the 'Reason Code' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        site_id (int): TODO: type description here.
        code (str): TODO: type description here.
        description (str): TODO: type description here.
        position (int): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "site_id": 'site_id',
        "code": 'code',
        "description": 'description',
        "position": 'position',
        "created_at": 'created_at',
        "updated_at": 'updated_at'
    }

    _optionals = [
        'id',
        'site_id',
        'code',
        'description',
        'position',
        'created_at',
        'updated_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 position=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP):
        """Constructor for the ReasonCode class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        if position is not APIHelper.SKIP:
            self.position = position 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        position = dictionary.get("position") if dictionary.get("position") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   site_id,
                   code,
                   description,
                   position,
                   created_at,
                   updated_at)
