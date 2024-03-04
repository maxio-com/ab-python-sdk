# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CancellationOptions(object):

    """Implementation of the 'Cancellation Options' model.

    TODO: type model description here.

    Attributes:
        cancellation_message (str): For your internal use. An indication as to
            why the subscription is being canceled.
        reason_code (str): The reason code associated with the cancellation.
            See the list of reason codes associated with your site.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cancellation_message": 'cancellation_message',
        "reason_code": 'reason_code'
    }

    _optionals = [
        'cancellation_message',
        'reason_code',
    ]

    def __init__(self,
                 cancellation_message=APIHelper.SKIP,
                 reason_code=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CancellationOptions class"""

        # Initialize members of the class
        if cancellation_message is not APIHelper.SKIP:
            self.cancellation_message = cancellation_message 
        if reason_code is not APIHelper.SKIP:
            self.reason_code = reason_code 

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
        cancellation_message = dictionary.get("cancellation_message") if dictionary.get("cancellation_message") else APIHelper.SKIP
        reason_code = dictionary.get("reason_code") if dictionary.get("reason_code") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(cancellation_message,
                   reason_code,
                   dictionary)
