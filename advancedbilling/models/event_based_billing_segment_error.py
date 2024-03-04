# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class EventBasedBillingSegmentError(object):

    """Implementation of the 'Event Based Billing Segment Error' model.

    TODO: type model description here.

    Attributes:
        segments (Dict[str, object]): The key of the object would be a number
            (an index in the request array) where the error occurred. In the
            value object, the key represents the field and the value is an
            array with error messages. In most cases, this object would
            contain just one key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segments": 'segments'
    }

    def __init__(self,
                 segments=None,
                 additional_properties={}):
        """Constructor for the EventBasedBillingSegmentError class"""

        # Initialize members of the class
        self.segments = segments 

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
        segments = dictionary.get("segments") if dictionary.get("segments") else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(segments,
                   dictionary)
