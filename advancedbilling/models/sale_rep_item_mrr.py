# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SaleRepItemMrr(object):

    """Implementation of the 'Sale Rep Item Mrr' model.

    TODO: type model description here.

    Attributes:
        mrr (str): TODO: type description here.
        usage (str): TODO: type description here.
        recurring (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mrr": 'mrr',
        "usage": 'usage',
        "recurring": 'recurring'
    }

    _optionals = [
        'mrr',
        'usage',
        'recurring',
    ]

    def __init__(self,
                 mrr=APIHelper.SKIP,
                 usage=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the SaleRepItemMrr class"""

        # Initialize members of the class
        if mrr is not APIHelper.SKIP:
            self.mrr = mrr 
        if usage is not APIHelper.SKIP:
            self.usage = usage 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 

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
        mrr = dictionary.get("mrr") if dictionary.get("mrr") else APIHelper.SKIP
        usage = dictionary.get("usage") if dictionary.get("usage") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if dictionary.get("recurring") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(mrr,
                   usage,
                   recurring,
                   dictionary)
