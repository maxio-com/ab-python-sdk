# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Proration(object):

    """Implementation of the 'Proration' model.

    TODO: type model description here.

    Attributes:
        preserve_period (bool): The alternative to sending preserve_period as
            a direct attribute to migration

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "preserve_period": 'preserve_period'
    }

    _optionals = [
        'preserve_period',
    ]

    def __init__(self,
                 preserve_period=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the Proration class"""

        # Initialize members of the class
        if preserve_period is not APIHelper.SKIP:
            self.preserve_period = preserve_period 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        preserve_period = dictionary.get("preserve_period") if "preserve_period" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(preserve_period,
                   dictionary)
