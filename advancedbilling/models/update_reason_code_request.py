# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.update_reason_code import UpdateReasonCode


class UpdateReasonCodeRequest(object):

    """Implementation of the 'Update Reason Code Request' model.

    TODO: type model description here.

    Attributes:
        reason_code (UpdateReasonCode): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason_code": 'reason_code'
    }

    def __init__(self,
                 reason_code=None,
                 additional_properties=None):
        """Constructor for the UpdateReasonCodeRequest class"""

        # Initialize members of the class
        self.reason_code = reason_code 

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
        reason_code = UpdateReasonCode.from_dictionary(dictionary.get('reason_code')) if dictionary.get('reason_code') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(reason_code,
                   additional_properties)
