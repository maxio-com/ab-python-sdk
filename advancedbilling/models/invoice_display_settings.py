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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the InvoiceDisplaySettings class"""

        # Initialize members of the class
        if hide_zero_subtotal_lines is not APIHelper.SKIP:
            self.hide_zero_subtotal_lines = hide_zero_subtotal_lines 
        if include_discounts_on_lines is not APIHelper.SKIP:
            self.include_discounts_on_lines = include_discounts_on_lines 

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
        hide_zero_subtotal_lines = dictionary.get("hide_zero_subtotal_lines") if "hide_zero_subtotal_lines" in dictionary.keys() else APIHelper.SKIP
        include_discounts_on_lines = dictionary.get("include_discounts_on_lines") if "include_discounts_on_lines" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(hide_zero_subtotal_lines,
                   include_discounts_on_lines,
                   additional_properties)

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
