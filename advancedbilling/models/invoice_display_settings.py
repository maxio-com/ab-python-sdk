# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceDisplaySettings(object):

    """Implementation of the 'Invoice Display Settings' model.

    TODO: type model description here.

    Attributes:
        hide_zero_subtotal_lines (bool): TODO: type description here.
        include_discounts_on_lines (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hide_zero_subtotal_lines": 'hide_zero_subtotal_lines',
        "include_discounts_on_lines": 'include_discounts_on_lines'
    }

    _optionals = [
        'hide_zero_subtotal_lines',
        'include_discounts_on_lines',
    ]

    def __init__(self,
                 hide_zero_subtotal_lines=APIHelper.SKIP,
                 include_discounts_on_lines=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoiceDisplaySettings class"""

        # Initialize members of the class
        if hide_zero_subtotal_lines is not APIHelper.SKIP:
            self.hide_zero_subtotal_lines = hide_zero_subtotal_lines 
        if include_discounts_on_lines is not APIHelper.SKIP:
            self.include_discounts_on_lines = include_discounts_on_lines 

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
        hide_zero_subtotal_lines = dictionary.get("hide_zero_subtotal_lines") if "hide_zero_subtotal_lines" in dictionary.keys() else APIHelper.SKIP
        include_discounts_on_lines = dictionary.get("include_discounts_on_lines") if "include_discounts_on_lines" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(hide_zero_subtotal_lines,
                   include_discounts_on_lines,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
