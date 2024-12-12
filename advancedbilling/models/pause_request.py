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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the PauseRequest class"""

        # Initialize members of the class
        if hold is not APIHelper.SKIP:
            self.hold = hold 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        hold = AutoResume.from_dictionary(dictionary.get('hold')) if 'hold' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(hold,
                   additional_properties)
