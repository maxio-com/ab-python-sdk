# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.mrr import MRR


class MRRResponse(object):

    """Implementation of the 'MRR response' model.

    TODO: type model description here.

    Attributes:
        mrr (MRR): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mrr": 'mrr'
    }

    def __init__(self,
                 mrr=None):
        """Constructor for the MRRResponse class"""

        # Initialize members of the class
        self.mrr = mrr 

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
        mrr = MRR.from_dictionary(dictionary.get('mrr')) if dictionary.get('mrr') else None
        # Return an object of this model
        return cls(mrr)
