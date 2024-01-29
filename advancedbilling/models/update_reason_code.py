# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateReasonCode(object):

    """Implementation of the 'Update Reason Code' model.

    TODO: type model description here.

    Attributes:
        code (str): The unique identifier for the ReasonCode
        description (str): The friendly summary of what the code signifies
        position (int): The order that code appears in lists

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "description": 'description',
        "position": 'position'
    }

    _optionals = [
        'code',
        'description',
        'position',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 position=APIHelper.SKIP):
        """Constructor for the UpdateReasonCode class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        if position is not APIHelper.SKIP:
            self.position = position 

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
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        position = dictionary.get("position") if dictionary.get("position") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   description,
                   position)
