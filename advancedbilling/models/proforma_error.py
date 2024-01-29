# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.base_string_error import BaseStringError


class ProformaError(object):

    """Implementation of the 'Proforma Error' model.

    TODO: type model description here.

    Attributes:
        subscription (BaseStringError): The error is base if it is not
            directly associated with a single attribute.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription": 'subscription'
    }

    _optionals = [
        'subscription',
    ]

    def __init__(self,
                 subscription=APIHelper.SKIP):
        """Constructor for the ProformaError class"""

        # Initialize members of the class
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 

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
        subscription = BaseStringError.from_dictionary(dictionary.get('subscription')) if 'subscription' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription)
