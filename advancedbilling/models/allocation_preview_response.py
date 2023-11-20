# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.allocation_preview import AllocationPreview


class AllocationPreviewResponse(object):

    """Implementation of the 'Allocation Preview Response' model.

    TODO: type model description here.

    Attributes:
        allocation_preview (AllocationPreview): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocation_preview": 'allocation_preview'
    }

    def __init__(self,
                 allocation_preview=None):
        """Constructor for the AllocationPreviewResponse class"""

        # Initialize members of the class
        self.allocation_preview = allocation_preview 

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
        allocation_preview = AllocationPreview.from_dictionary(dictionary.get('allocation_preview')) if dictionary.get('allocation_preview') else None
        # Return an object of this model
        return cls(allocation_preview)
