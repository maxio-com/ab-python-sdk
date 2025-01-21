# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PayerError(object):

    """Implementation of the 'Payer Error' model.

    Attributes:
        last_name (List[str]): The model property of type List[str].
        first_name (List[str]): The model property of type List[str].
        email (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_name": 'last_name',
        "first_name": 'first_name',
        "email": 'email'
    }

    _optionals = [
        'last_name',
        'first_name',
        'email',
    ]

    def __init__(self,
                 last_name=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PayerError class"""

        # Initialize members of the class
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
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
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(last_name,
                   first_name,
                   email,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'last_name={self.last_name!r}, '
                f'first_name={self.first_name!r}, '
                f'email={self.email!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'last_name={self.last_name!s}, '
                f'first_name={self.first_name!s}, '
                f'email={self.email!s}, '
                f'additional_properties={self.additional_properties!s})')
