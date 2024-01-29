# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class VoidInvoice(object):

    """Implementation of the 'Void Invoice' model.

    TODO: type model description here.

    Attributes:
        reason (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason'
    }

    def __init__(self,
                 reason=None):
        """Constructor for the VoidInvoice class"""

        # Initialize members of the class
        self.reason = reason 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        # Return an object of this model
        return cls(reason)
