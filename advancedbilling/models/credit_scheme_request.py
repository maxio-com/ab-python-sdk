# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreditSchemeRequest(object):

    """Implementation of the 'Credit Scheme Request' model.

    TODO: type model description here.

    Attributes:
        credit_scheme (CreditScheme): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_scheme": 'credit_scheme'
    }

    def __init__(self,
                 credit_scheme=None,
                 additional_properties={}):
        """Constructor for the CreditSchemeRequest class"""

        # Initialize members of the class
        self.credit_scheme = credit_scheme 

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
        credit_scheme = dictionary.get("credit_scheme") if dictionary.get("credit_scheme") else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(credit_scheme,
                   dictionary)
