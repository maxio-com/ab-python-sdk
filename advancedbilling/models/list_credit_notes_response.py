# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.credit_note import CreditNote


class ListCreditNotesResponse(object):

    """Implementation of the 'List Credit Notes Response' model.

    Attributes:
        credit_notes (List[CreditNote]): The model property of type
            List[CreditNote].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_notes": 'credit_notes'
    }

    def __init__(self,
                 credit_notes=None,
                 additional_properties=None):
        """Constructor for the ListCreditNotesResponse class"""

        # Initialize members of the class
        self.credit_notes = credit_notes 

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
        credit_notes = None
        if dictionary.get('credit_notes') is not None:
            credit_notes = [CreditNote.from_dictionary(x) for x in dictionary.get('credit_notes')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(credit_notes,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'credit_notes={self.credit_notes!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'credit_notes={self.credit_notes!s}, '
                f'additional_properties={self.additional_properties!s})')
