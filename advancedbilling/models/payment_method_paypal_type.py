# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentMethodPaypalType(object):

    """Implementation of the 'Payment Method Paypal Type' model.

    TODO: type model description here.

    Attributes:
        email (str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": 'email',
        "mtype": 'type'
    }

    _optionals = [
        'email',
        'mtype',
    ]

    def __init__(self,
                 email=APIHelper.SKIP,
                 mtype='paypal_account'):
        """Constructor for the PaymentMethodPaypalType class"""

        # Initialize members of the class
        if email is not APIHelper.SKIP:
            self.email = email 
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
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'paypal_account'
        # Return an object of this model
        return cls(email,
                   mtype)

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
