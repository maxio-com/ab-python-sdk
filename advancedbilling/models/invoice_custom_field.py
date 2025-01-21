# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceCustomField(object):

    """Implementation of the 'Invoice Custom Field' model.

    Attributes:
        owner_id (int): The model property of type int.
        owner_type (CustomFieldOwner): The model property of type
            CustomFieldOwner.
        name (str): The model property of type str.
        value (str): The model property of type str.
        metadatum_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 metadatum_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceCustomField class"""

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
        owner_id = dictionary.get("owner_id") if dictionary.get("owner_id") else APIHelper.SKIP
        owner_type = dictionary.get("owner_type") if dictionary.get("owner_type") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        metadatum_id = dictionary.get("metadatum_id") if dictionary.get("metadatum_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(owner_id,
                   owner_type,
                   name,
                   value,
                   metadatum_id,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'owner_id={self.owner_id!r}, '
                f'owner_type={self.owner_type!r}, '
                f'name={self.name!r}, '
                f'value={self.value!r}, '
                f'metadatum_id={self.metadatum_id!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'owner_id={self.owner_id!s}, '
                f'owner_type={self.owner_type!s}, '
                f'name={self.name!s}, '
                f'value={self.value!s}, '
                f'metadatum_id={self.metadatum_id!s}, '
                f'additional_properties={self.additional_properties!s})')
