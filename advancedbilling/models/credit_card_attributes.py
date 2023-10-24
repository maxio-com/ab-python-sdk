# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreditCardAttributes(object):

    """Implementation of the 'Credit Card Attributes' model.

    TODO: type model description here.

    Attributes:
        full_number (str): TODO: type description here.
        expiration_month (str): TODO: type description here.
        expiration_year (str): TODO: type description here.

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
                 expiration_year=APIHelper.SKIP):
        """Constructor for the CreditCardAttributes class"""

        # Initialize members of the class
        if full_number is not APIHelper.SKIP:
            self.full_number = full_number 
        if expiration_month is not APIHelper.SKIP:
            self.expiration_month = expiration_month 
        if expiration_year is not APIHelper.SKIP:
            self.expiration_year = expiration_year 

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
        full_number = dictionary.get("full_number") if dictionary.get("full_number") else APIHelper.SKIP
        expiration_month = dictionary.get("expiration_month") if dictionary.get("expiration_month") else APIHelper.SKIP
        expiration_year = dictionary.get("expiration_year") if dictionary.get("expiration_year") else APIHelper.SKIP
        # Return an object of this model
        return cls(full_number,
                   expiration_month,
                   expiration_year)
