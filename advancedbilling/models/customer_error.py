# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomerError(object):

    """Implementation of the 'Customer Error' model.

    TODO: type model description here.

    Attributes:
        customer (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer": 'customer'
    }

    _optionals = [
        'customer',
    ]

    def __init__(self,
                 customer=APIHelper.SKIP):
        """Constructor for the CustomerError class"""

        # Initialize members of the class
        if customer is not APIHelper.SKIP:
            self.customer = customer 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        customer = dictionary.get("customer") if dictionary.get("customer") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer)

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
