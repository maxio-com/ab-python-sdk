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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_scheme": 'credit_scheme'
    }

    def __init__(self,
                 credit_scheme=None,
                 additional_properties=None):
        """Constructor for the CreditSchemeRequest class"""

        # Initialize members of the class
        self.credit_scheme = credit_scheme 

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
        credit_scheme = dictionary.get("credit_scheme") if dictionary.get("credit_scheme") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(credit_scheme,
                   additional_properties)
