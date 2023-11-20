# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AutoResume(object):

    """Implementation of the 'Auto Resume' model.

    TODO: type model description here.

    Attributes:
        automatically_resume_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "automatically_resume_at": 'automatically_resume_at'
    }

    _optionals = [
        'automatically_resume_at',
    ]

    def __init__(self,
                 automatically_resume_at=APIHelper.SKIP):
        """Constructor for the AutoResume class"""

        # Initialize members of the class
        if automatically_resume_at is not APIHelper.SKIP:
            self.automatically_resume_at = automatically_resume_at 

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
        automatically_resume_at = dictionary.get("automatically_resume_at") if dictionary.get("automatically_resume_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(automatically_resume_at)
