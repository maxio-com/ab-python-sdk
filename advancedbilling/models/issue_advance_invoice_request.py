# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class IssueAdvanceInvoiceRequest(object):

    """Implementation of the 'Issue Advance Invoice Request' model.

    TODO: type model description here.

    Attributes:
        force (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "force": 'force'
    }

    _optionals = [
        'force',
    ]

    def __init__(self,
                 force=APIHelper.SKIP):
        """Constructor for the IssueAdvanceInvoiceRequest class"""

        # Initialize members of the class
        if force is not APIHelper.SKIP:
            self.force = force 

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
        force = dictionary.get("force") if "force" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(force)
