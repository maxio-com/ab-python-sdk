# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.invoice_payer_change import InvoicePayerChange


class CustomerPayerChange(object):

    """Implementation of the 'Customer Payer Change' model.

    TODO: type model description here.

    Attributes:
        before (InvoicePayerChange): TODO: type description here.
        after (InvoicePayerChange): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": 'before',
        "after": 'after'
    }

    def __init__(self,
                 before=None,
                 after=None,
                 additional_properties={}):
        """Constructor for the CustomerPayerChange class"""

        # Initialize members of the class
        self.before = before 
        self.after = after 

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
        before = InvoicePayerChange.from_dictionary(dictionary.get('before')) if dictionary.get('before') else None
        after = InvoicePayerChange.from_dictionary(dictionary.get('after')) if dictionary.get('after') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(before,
                   after,
                   dictionary)
