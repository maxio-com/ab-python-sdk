# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceBalanceItem(object):

    """Implementation of the 'Invoice Balance Item' model.

    Attributes:
        uid (str): The model property of type str.
        number (str): The model property of type str.
        outstanding_amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "number": 'number',
        "outstanding_amount": 'outstanding_amount'
    }

    _optionals = [
        'uid',
        'number',
        'outstanding_amount',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 outstanding_amount=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceBalanceItem class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if number is not APIHelper.SKIP:
            self.number = number 
        if outstanding_amount is not APIHelper.SKIP:
            self.outstanding_amount = outstanding_amount 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        outstanding_amount = dictionary.get("outstanding_amount") if dictionary.get("outstanding_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   number,
                   outstanding_amount,
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
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'number={(self.number if hasattr(self, "number") else None)!r}, '
                f'outstanding_amount={(self.outstanding_amount if hasattr(self, "outstanding_amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'number={(self.number if hasattr(self, "number") else None)!s}, '
                f'outstanding_amount={(self.outstanding_amount if hasattr(self, "outstanding_amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
