# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.reason_code import ReasonCode


class ReasonCodeResponse(object):

    """Implementation of the 'Reason Code Response' model.

    TODO: type model description here.

    Attributes:
        reason_code (ReasonCode): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason_code": 'reason_code'
    }

    def __init__(self,
                 reason_code=None):
        """Constructor for the ReasonCodeResponse class"""

        # Initialize members of the class
        self.reason_code = reason_code 

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
        reason_code = ReasonCode.from_dictionary(dictionary.get('reason_code')) if dictionary.get('reason_code') else None
        # Return an object of this model
        return cls(reason_code)
