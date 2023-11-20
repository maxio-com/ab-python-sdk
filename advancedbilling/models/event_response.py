# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.event import Event


class EventResponse(object):

    """Implementation of the 'Event Response' model.

    TODO: type model description here.

    Attributes:
        event (Event): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event": 'event'
    }

    def __init__(self,
                 event=None):
        """Constructor for the EventResponse class"""

        # Initialize members of the class
        self.event = event 

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
        event = Event.from_dictionary(dictionary.get('event')) if dictionary.get('event') else None
        # Return an object of this model
        return cls(event)
