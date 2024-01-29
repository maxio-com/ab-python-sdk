# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceCustomField(object):

    """Implementation of the 'Invoice Custom Field' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        value (str): TODO: type description here.
        owner_id (int): TODO: type description here.
        owner_type (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "value": 'value',
        "owner_id": 'owner_id',
        "owner_type": 'owner_type'
    }

    _optionals = [
        'name',
        'value',
        'owner_id',
        'owner_type',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 owner_id=APIHelper.SKIP,
                 owner_type=APIHelper.SKIP):
        """Constructor for the InvoiceCustomField class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 
        if owner_id is not APIHelper.SKIP:
            self.owner_id = owner_id 
        if owner_type is not APIHelper.SKIP:
            self.owner_type = owner_type 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        owner_id = dictionary.get("owner_id") if dictionary.get("owner_id") else APIHelper.SKIP
        owner_type = dictionary.get("owner_type") if dictionary.get("owner_type") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   value,
                   owner_id,
                   owner_type)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
