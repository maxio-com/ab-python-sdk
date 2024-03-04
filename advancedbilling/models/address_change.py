# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress


class AddressChange(object):

    """Implementation of the 'Address Change' model.

    TODO: type model description here.

    Attributes:
        before (InvoiceAddress): TODO: type description here.
        after (InvoiceAddress): TODO: type description here.

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
        """Constructor for the AddressChange class"""

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
        before = InvoiceAddress.from_dictionary(dictionary.get('before')) if dictionary.get('before') else None
        after = InvoiceAddress.from_dictionary(dictionary.get('after')) if dictionary.get('after') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(before,
                   after,
                   dictionary)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.before, type_callable=lambda value: InvoiceAddress.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.after, type_callable=lambda value: InvoiceAddress.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('before'), type_callable=lambda value: InvoiceAddress.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('after'), type_callable=lambda value: InvoiceAddress.validate(value))
