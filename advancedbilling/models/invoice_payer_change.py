# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePayerChange(object):

    """Implementation of the 'Invoice Payer Change' model.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        organization (str): The model property of type str.
        email (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "organization": 'organization',
        "email": 'email'
    }

    _optionals = [
        'first_name',
        'last_name',
        'organization',
        'email',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoicePayerChange class"""

        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if organization is not APIHelper.SKIP:
            self.organization = organization 
        if email is not APIHelper.SKIP:
            self.email = email 

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
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        organization = dictionary.get("organization") if dictionary.get("organization") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   organization,
                   email,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!r}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!r}, '
                f'organization={(self.organization if hasattr(self, "organization") else None)!r}, '
                f'email={(self.email if hasattr(self, "email") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!s}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!s}, '
                f'organization={(self.organization if hasattr(self, "organization") else None)!s}, '
                f'email={(self.email if hasattr(self, "email") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
