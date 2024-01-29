# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_allocation import CreateAllocation


class CreateAllocationRequest(object):

    """Implementation of the 'Create Allocation Request' model.

    TODO: type model description here.

    Attributes:
        allocation (CreateAllocation): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocation": 'allocation'
    }

    def __init__(self,
                 allocation=None):
        """Constructor for the CreateAllocationRequest class"""

        # Initialize members of the class
        self.allocation = allocation 

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
        allocation = CreateAllocation.from_dictionary(dictionary.get('allocation')) if dictionary.get('allocation') else None
        # Return an object of this model
        return cls(allocation)
