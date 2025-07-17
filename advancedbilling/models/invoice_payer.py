# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePayer(object):

    """Implementation of the 'Invoice Payer' model.

    Attributes:
        chargify_id (int): The model property of type int.
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        organization (str): The model property of type str.
        email (str): The model property of type str.
        vat_number (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_id": 'chargify_id',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "organization": 'organization',
        "email": 'email',
        "vat_number": 'vat_number'
    }

    _optionals = [
        'chargify_id',
        'first_name',
        'last_name',
        'organization',
        'email',
        'vat_number',
    ]

    _nullables = [
        'organization',
        'vat_number',
    ]

    def __init__(self,
                 chargify_id=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 vat_number=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoicePayer class"""

        # Initialize members of the class
        if chargify_id is not APIHelper.SKIP:
            self.chargify_id = chargify_id 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if organization is not APIHelper.SKIP:
            self.organization = organization 
        if email is not APIHelper.SKIP:
            self.email = email 
        if vat_number is not APIHelper.SKIP:
            self.vat_number = vat_number 

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
        chargify_id = dictionary.get("chargify_id") if dictionary.get("chargify_id") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        organization = dictionary.get("organization") if "organization" in dictionary.keys() else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        vat_number = dictionary.get("vat_number") if "vat_number" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(chargify_id,
                   first_name,
                   last_name,
                   organization,
                   email,
                   vat_number,
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
                f'chargify_id={(self.chargify_id if hasattr(self, "chargify_id") else None)!r}, '
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!r}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!r}, '
                f'organization={(self.organization if hasattr(self, "organization") else None)!r}, '
                f'email={(self.email if hasattr(self, "email") else None)!r}, '
                f'vat_number={(self.vat_number if hasattr(self, "vat_number") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'chargify_id={(self.chargify_id if hasattr(self, "chargify_id") else None)!s}, '
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!s}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!s}, '
                f'organization={(self.organization if hasattr(self, "organization") else None)!s}, '
                f'email={(self.email if hasattr(self, "email") else None)!s}, '
                f'vat_number={(self.vat_number if hasattr(self, "vat_number") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
