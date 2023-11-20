# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BaseStringError(object):

    """Implementation of the 'Base String Error' model.

    The error is base if it is not directly associated with a single
    attribute.

    Attributes:
        base (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base": 'base'
    }

    _optionals = [
        'base',
    ]

    def __init__(self,
                 base=APIHelper.SKIP):
        """Constructor for the BaseStringError class"""

        # Initialize members of the class
        if base is not APIHelper.SKIP:
            self.base = base 

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
        base = dictionary.get("base") if dictionary.get("base") else APIHelper.SKIP
        # Return an object of this model
        return cls(base)
