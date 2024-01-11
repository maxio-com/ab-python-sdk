# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentMethodApplePayType(object):

    """Implementation of the 'Payment Method Apple Pay Type' model.

    TODO: type model description here.

    Attributes:
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type'
    }

    _optionals = [
        'mtype',
    ]

    def __init__(self,
                 mtype='apple_pay'):
        """Constructor for the PaymentMethodApplePayType class"""

        # Initialize members of the class
        self.mtype = mtype 

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
        mtype = dictionary.get("type") if dictionary.get("type") else 'apple_pay'
        # Return an object of this model
        return cls(mtype)

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
