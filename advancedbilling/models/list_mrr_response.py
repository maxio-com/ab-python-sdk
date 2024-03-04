# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.list_mrr_response_result import ListMRRResponseResult


class ListMRRResponse(object):

    """Implementation of the 'List MRR Response' model.

    TODO: type model description here.

    Attributes:
        mrr (ListMRRResponseResult): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mrr": 'mrr'
    }

    def __init__(self,
                 mrr=None,
                 additional_properties={}):
        """Constructor for the ListMRRResponse class"""

        # Initialize members of the class
        self.mrr = mrr 

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
        mrr = ListMRRResponseResult.from_dictionary(dictionary.get('mrr')) if dictionary.get('mrr') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(mrr,
                   dictionary)
