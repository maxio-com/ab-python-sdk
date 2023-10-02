# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper


class Errors(object):

    """Implementation of the 'Errors' model.

    TODO: type model description here.

    Attributes:
        error (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'error'
    }

    _optionals = [
        'error',
    ]

    def __init__(self,
                 error=APIHelper.SKIP):
        """Constructor for the Errors class"""

        # Initialize members of the class
        if error is not APIHelper.SKIP:
            self.error = error 

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
        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        # Return an object of this model
        return cls(error)
