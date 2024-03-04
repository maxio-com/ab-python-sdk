# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.auto_resume import AutoResume


class PauseRequest(object):

    """Implementation of the 'Pause Request' model.

    Allows to pause a Subscription

    Attributes:
        hold (AutoResume): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hold": 'hold'
    }

    _optionals = [
        'hold',
    ]

    def __init__(self,
                 hold=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the PauseRequest class"""

        # Initialize members of the class
        if hold is not APIHelper.SKIP:
            self.hold = hold 

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
        hold = AutoResume.from_dictionary(dictionary.get('hold')) if 'hold' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(hold,
                   dictionary)
