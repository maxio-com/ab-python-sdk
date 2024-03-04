# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.update_subscription_note import UpdateSubscriptionNote


class UpdateSubscriptionNoteRequest(object):

    """Implementation of the 'Update Subscription Note Request' model.

    Updatable fields for Subscription Note

    Attributes:
        note (UpdateSubscriptionNote): Updatable fields for Subscription Note

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "note": 'note'
    }

    def __init__(self,
                 note=None,
                 additional_properties={}):
        """Constructor for the UpdateSubscriptionNoteRequest class"""

        # Initialize members of the class
        self.note = note 

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
        note = UpdateSubscriptionNote.from_dictionary(dictionary.get('note')) if dictionary.get('note') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(note,
                   dictionary)
