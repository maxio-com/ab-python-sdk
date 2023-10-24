# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProformaCustomField(object):

    """Implementation of the 'Proforma Custom Field' model.

    TODO: type model description here.

    Attributes:
        owner_id (float): TODO: type description here.
        owner_type (str): TODO: type description here.
        name (str): TODO: type description here.
        value (str): TODO: type description here.
        metadatum_id (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "owner_id": 'owner_id',
        "owner_type": 'owner_type',
        "name": 'name',
        "value": 'value',
        "metadatum_id": 'metadatum_id'
    }

    _optionals = [
        'owner_id',
        'owner_type',
        'name',
        'value',
        'metadatum_id',
    ]

    def __init__(self,
                 owner_id=APIHelper.SKIP,
                 owner_type=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 metadatum_id=APIHelper.SKIP):
        """Constructor for the ProformaCustomField class"""

        # Initialize members of the class
        if owner_id is not APIHelper.SKIP:
            self.owner_id = owner_id 
        if owner_type is not APIHelper.SKIP:
            self.owner_type = owner_type 
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 
        if metadatum_id is not APIHelper.SKIP:
            self.metadatum_id = metadatum_id 

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
        owner_id = dictionary.get("owner_id") if dictionary.get("owner_id") else APIHelper.SKIP
        owner_type = dictionary.get("owner_type") if dictionary.get("owner_type") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        metadatum_id = dictionary.get("metadatum_id") if dictionary.get("metadatum_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(owner_id,
                   owner_type,
                   name,
                   value,
                   metadatum_id)
