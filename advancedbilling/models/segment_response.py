# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.segment import Segment


class SegmentResponse(object):

    """Implementation of the 'Segment Response' model.

    TODO: type model description here.

    Attributes:
        segment (Segment): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segment": 'segment'
    }

    _optionals = [
        'segment',
    ]

    def __init__(self,
                 segment=APIHelper.SKIP):
        """Constructor for the SegmentResponse class"""

        # Initialize members of the class
        if segment is not APIHelper.SKIP:
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
        segment = Segment.from_dictionary(dictionary.get('segment')) if 'segment' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(segment)
