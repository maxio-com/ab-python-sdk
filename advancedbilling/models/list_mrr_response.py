# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.list_mrr_response_result import ListMRRResponseResult


class ListMRRResponse(object):

    """Implementation of the 'List MRR Response' model.

    Attributes:
        mrr (ListMRRResponseResult): The model property of type
            ListMRRResponseResult.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mrr": 'mrr'
    }

    def __init__(self,
                 mrr=None,
                 additional_properties=None):
        """Constructor for the ListMRRResponse class"""

        # Initialize members of the class
        self.mrr = mrr 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        mrr = ListMRRResponseResult.from_dictionary(dictionary.get('mrr')) if dictionary.get('mrr') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(mrr,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mrr={self.mrr!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mrr={self.mrr!s}, '
                f'additional_properties={self.additional_properties!s})')
