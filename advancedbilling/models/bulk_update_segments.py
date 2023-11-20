# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.bulk_update_segments_item import BulkUpdateSegmentsItem


class BulkUpdateSegments(object):

    """Implementation of the 'Bulk Update Segments' model.

    TODO: type model description here.

    Attributes:
        segments (List[BulkUpdateSegmentsItem]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segments": 'segments'
    }

    _optionals = [
        'segments',
    ]

    def __init__(self,
                 segments=APIHelper.SKIP):
        """Constructor for the BulkUpdateSegments class"""

        # Initialize members of the class
        if segments is not APIHelper.SKIP:
            self.segments = segments 

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
        segments = None
        if dictionary.get('segments') is not None:
            segments = [BulkUpdateSegmentsItem.from_dictionary(x) for x in dictionary.get('segments')]
        else:
            segments = APIHelper.SKIP
        # Return an object of this model
        return cls(segments)
