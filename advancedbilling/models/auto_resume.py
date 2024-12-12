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
        automatically_resume_at (datetime): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "automatically_resume_at": 'automatically_resume_at'
    }

    _optionals = [
        'automatically_resume_at',
    ]

    _nullables = [
        'automatically_resume_at',
    ]

    def __init__(self,
                 automatically_resume_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AutoResume class"""

        # Initialize members of the class
        if automatically_resume_at is not APIHelper.SKIP:
            self.automatically_resume_at = APIHelper.apply_datetime_converter(automatically_resume_at, APIHelper.RFC3339DateTime) if automatically_resume_at else None 

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
        if 'automatically_resume_at' in dictionary.keys():
            automatically_resume_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("automatically_resume_at")).datetime if dictionary.get("automatically_resume_at") else None
        else:
            automatically_resume_at = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(automatically_resume_at,
                   additional_properties)
