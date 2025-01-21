# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreditCardAttributes(object):

    """Implementation of the 'Credit Card Attributes' model.

    Attributes:
        full_number (str): The model property of type str.
        expiration_month (str): The model property of type str.
        expiration_year (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "full_number": 'full_number',
        "expiration_month": 'expiration_month',
        "expiration_year": 'expiration_year'
    }

    _optionals = [
        'full_number',
        'expiration_month',
        'expiration_year',
    ]

    def __init__(self,
                 full_number=APIHelper.SKIP,
                 expiration_month=APIHelper.SKIP,
                 expiration_year=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreditCardAttributes class"""

        # Initialize members of the class
        if full_number is not APIHelper.SKIP:
            self.full_number = full_number 
        if expiration_month is not APIHelper.SKIP:
            self.expiration_month = expiration_month 
        if expiration_year is not APIHelper.SKIP:
            self.expiration_year = expiration_year 

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
        full_number = dictionary.get("full_number") if dictionary.get("full_number") else APIHelper.SKIP
        expiration_month = dictionary.get("expiration_month") if dictionary.get("expiration_month") else APIHelper.SKIP
        expiration_year = dictionary.get("expiration_year") if dictionary.get("expiration_year") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(full_number,
                   expiration_month,
                   expiration_year,
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
                f'full_number={self.full_number!r}, '
                f'expiration_month={self.expiration_month!r}, '
                f'expiration_year={self.expiration_year!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'full_number={self.full_number!s}, '
                f'expiration_month={self.expiration_month!s}, '
                f'expiration_year={self.expiration_year!s}, '
                f'additional_properties={self.additional_properties!s})')
