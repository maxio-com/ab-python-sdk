# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PendingCancellationChange(object):

    """Implementation of the 'Pending Cancellation Change' model.

    TODO: type model description here.

    Attributes:
        cancellation_state (str): TODO: type description here.
        cancels_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cancellation_state": 'cancellation_state',
        "cancels_at": 'cancels_at'
    }

    def __init__(self,
                 cancellation_state=None,
                 cancels_at=None):
        """Constructor for the PendingCancellationChange class"""

        # Initialize members of the class
        self.cancellation_state = cancellation_state 
        self.cancels_at = cancels_at 

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
        cancellation_state = dictionary.get("cancellation_state") if dictionary.get("cancellation_state") else None
        cancels_at = dictionary.get("cancels_at") if dictionary.get("cancels_at") else None
        # Return an object of this model
        return cls(cancellation_state,
                   cancels_at)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.cancellation_state, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.cancels_at, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('cancellation_state'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('cancels_at'), type_callable=lambda value: isinstance(value, str))
