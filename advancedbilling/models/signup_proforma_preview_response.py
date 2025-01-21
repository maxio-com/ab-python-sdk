# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.signup_proforma_preview import SignupProformaPreview


class SignupProformaPreviewResponse(object):

    """Implementation of the 'Signup Proforma Preview Response' model.

    Attributes:
        proforma_invoice_preview (SignupProformaPreview): The model property
            of type SignupProformaPreview.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "proforma_invoice_preview": 'proforma_invoice_preview'
    }

    def __init__(self,
                 proforma_invoice_preview=None,
                 additional_properties=None):
        """Constructor for the SignupProformaPreviewResponse class"""

        # Initialize members of the class
        self.proforma_invoice_preview = proforma_invoice_preview 

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
        proforma_invoice_preview = SignupProformaPreview.from_dictionary(dictionary.get('proforma_invoice_preview')) if dictionary.get('proforma_invoice_preview') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(proforma_invoice_preview,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'proforma_invoice_preview={self.proforma_invoice_preview!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'proforma_invoice_preview={self.proforma_invoice_preview!s}, '
                f'additional_properties={self.additional_properties!s})')
