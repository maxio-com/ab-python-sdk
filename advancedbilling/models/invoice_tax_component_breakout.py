# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceTaxComponentBreakout(object):

    """Implementation of the 'Invoice Tax Component Breakout' model.

    TODO: type model description here.

    Attributes:
        tax_rule_id (int): TODO: type description here.
        percentage (str): TODO: type description here.
        country_code (str): TODO: type description here.
        subdivision_code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax_rule_id": 'tax_rule_id',
        "percentage": 'percentage',
        "country_code": 'country_code',
        "subdivision_code": 'subdivision_code'
    }

    _optionals = [
        'tax_rule_id',
        'percentage',
        'country_code',
        'subdivision_code',
    ]

    def __init__(self,
                 tax_rule_id=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 subdivision_code=APIHelper.SKIP):
        """Constructor for the InvoiceTaxComponentBreakout class"""

        # Initialize members of the class
        if tax_rule_id is not APIHelper.SKIP:
            self.tax_rule_id = tax_rule_id 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if subdivision_code is not APIHelper.SKIP:
            self.subdivision_code = subdivision_code 

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
        tax_rule_id = dictionary.get("tax_rule_id") if dictionary.get("tax_rule_id") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        country_code = dictionary.get("country_code") if dictionary.get("country_code") else APIHelper.SKIP
        subdivision_code = dictionary.get("subdivision_code") if dictionary.get("subdivision_code") else APIHelper.SKIP
        # Return an object of this model
        return cls(tax_rule_id,
                   percentage,
                   country_code,
                   subdivision_code)
