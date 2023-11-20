# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.customer_change import CustomerChange


class CustomerChangesPreviewResponse(object):

    """Implementation of the 'Customer Changes Preview Response' model.

    TODO: type model description here.

    Attributes:
        changes (CustomerChange): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "changes": 'changes'
    }

    def __init__(self,
                 changes=None):
        """Constructor for the CustomerChangesPreviewResponse class"""

        # Initialize members of the class
        self.changes = changes 

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
        changes = CustomerChange.from_dictionary(dictionary.get('changes')) if dictionary.get('changes') else None
        # Return an object of this model
        return cls(changes)
