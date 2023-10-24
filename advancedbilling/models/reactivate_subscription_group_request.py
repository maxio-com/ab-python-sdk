# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReactivateSubscriptionGroupRequest(object):

    """Implementation of the 'Reactivate Subscription Group Request' model.

    TODO: type model description here.

    Attributes:
        resume (bool): TODO: type description here.
        resume_members (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resume": 'resume',
        "resume_members": 'resume_members'
    }

    _optionals = [
        'resume',
        'resume_members',
    ]

    def __init__(self,
                 resume=APIHelper.SKIP,
                 resume_members=APIHelper.SKIP):
        """Constructor for the ReactivateSubscriptionGroupRequest class"""

        # Initialize members of the class
        if resume is not APIHelper.SKIP:
            self.resume = resume 
        if resume_members is not APIHelper.SKIP:
            self.resume_members = resume_members 

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
        resume = dictionary.get("resume") if "resume" in dictionary.keys() else APIHelper.SKIP
        resume_members = dictionary.get("resume_members") if "resume_members" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(resume,
                   resume_members)
