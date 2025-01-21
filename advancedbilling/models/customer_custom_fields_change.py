# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.invoice_custom_field import InvoiceCustomField


class CustomerCustomFieldsChange(object):

    """Implementation of the 'Customer Custom Fields Change' model.

    Attributes:
        before (List[InvoiceCustomField]): The model property of type
            List[InvoiceCustomField].
        after (List[InvoiceCustomField]): The model property of type
            List[InvoiceCustomField].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": 'before',
        "after": 'after'
    }

    def __init__(self,
                 before=None,
                 after=None,
                 additional_properties=None):
        """Constructor for the CustomerCustomFieldsChange class"""

        # Initialize members of the class
        self.before = before 
        self.after = after 

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
        before = None
        if dictionary.get('before') is not None:
            before = [InvoiceCustomField.from_dictionary(x) for x in dictionary.get('before')]
        after = None
        if dictionary.get('after') is not None:
            after = [InvoiceCustomField.from_dictionary(x) for x in dictionary.get('after')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(before,
                   after,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'before={self.before!r}, '
                f'after={self.after!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'before={self.before!s}, '
                f'after={self.after!s}, '
                f'additional_properties={self.additional_properties!s})')
