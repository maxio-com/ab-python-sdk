# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_allocation import CreateAllocation


class PreviewAllocationsRequest(object):

    """Implementation of the 'Preview Allocations Request' model.

    TODO: type model description here.

    Attributes:
        allocations (List[CreateAllocation]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocations": 'allocations'
    }

    def __init__(self,
                 allocations=None):
        """Constructor for the PreviewAllocationsRequest class"""

        # Initialize members of the class
        self.allocations = allocations 

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
        allocations = None
        if dictionary.get('allocations') is not None:
            allocations = [CreateAllocation.from_dictionary(x) for x in dictionary.get('allocations')]
        # Return an object of this model
        return cls(allocations)
