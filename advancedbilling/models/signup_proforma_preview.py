# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.proforma_invoice import ProformaInvoice


class SignupProformaPreview(object):

    """Implementation of the 'Signup Proforma Preview' model.

    Attributes:
        current_proforma_invoice (ProformaInvoice): The model property of type
            ProformaInvoice.
        next_proforma_invoice (ProformaInvoice): The model property of type
            ProformaInvoice.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_proforma_invoice": 'current_proforma_invoice',
        "next_proforma_invoice": 'next_proforma_invoice'
    }

    _optionals = [
        'current_proforma_invoice',
        'next_proforma_invoice',
    ]

    def __init__(self,
                 current_proforma_invoice=APIHelper.SKIP,
                 next_proforma_invoice=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SignupProformaPreview class"""

        # Initialize members of the class
        if current_proforma_invoice is not APIHelper.SKIP:
            self.current_proforma_invoice = current_proforma_invoice 
        if next_proforma_invoice is not APIHelper.SKIP:
            self.next_proforma_invoice = next_proforma_invoice 

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
        current_proforma_invoice = ProformaInvoice.from_dictionary(dictionary.get('current_proforma_invoice')) if 'current_proforma_invoice' in dictionary.keys() else APIHelper.SKIP
        next_proforma_invoice = ProformaInvoice.from_dictionary(dictionary.get('next_proforma_invoice')) if 'next_proforma_invoice' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(current_proforma_invoice,
                   next_proforma_invoice,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'current_proforma_invoice={self.current_proforma_invoice!r}, '
                f'next_proforma_invoice={self.next_proforma_invoice!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'current_proforma_invoice={self.current_proforma_invoice!s}, '
                f'next_proforma_invoice={self.next_proforma_invoice!s}, '
                f'additional_properties={self.additional_properties!s})')
