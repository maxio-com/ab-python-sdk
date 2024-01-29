# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.update_segment import UpdateSegment


class UpdateSegmentRequest(object):

    """Implementation of the 'Update Segment Request' model.

    TODO: type model description here.

    Attributes:
        segment (UpdateSegment): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segment": 'segment'
    }

    def __init__(self,
                 segment=None):
        """Constructor for the UpdateSegmentRequest class"""

        # Initialize members of the class
        self.segment = segment 

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
        segment = UpdateSegment.from_dictionary(dictionary.get('segment')) if dictionary.get('segment') else None
        # Return an object of this model
        return cls(segment)
