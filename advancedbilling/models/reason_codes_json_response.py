# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReasonCodesJsonResponse(object):

    """Implementation of the 'Reason Codes Json Response' model.

    TODO: type model description here.

    Attributes:
        ok (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ok": 'ok'
    }

    _optionals = [
        'ok',
    ]

    def __init__(self,
                 ok=APIHelper.SKIP):
        """Constructor for the ReasonCodesJsonResponse class"""

        # Initialize members of the class
        if ok is not APIHelper.SKIP:
            self.ok = ok 

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
        ok = dictionary.get("ok") if dictionary.get("ok") else APIHelper.SKIP
        # Return an object of this model
        return cls(ok)
