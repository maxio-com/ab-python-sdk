# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceAddress(object):

    """Implementation of the 'Invoice Address' model.

    TODO: type model description here.

    Attributes:
        street (str): TODO: type description here.
        line_2 (str): TODO: type description here.
        city (str): TODO: type description here.
        state (str): TODO: type description here.
        zip (str): TODO: type description here.
        country (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "street": 'street',
        "line_2": 'line2',
        "city": 'city',
        "state": 'state',
        "zip": 'zip',
        "country": 'country'
    }

    _optionals = [
        'street',
        'line_2',
        'city',
        'state',
        'zip',
        'country',
    ]

    _nullables = [
        'street',
        'line_2',
        'city',
        'state',
        'zip',
        'country',
    ]

    def __init__(self,
                 street=APIHelper.SKIP,
                 line_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 country=APIHelper.SKIP):
        """Constructor for the InvoiceAddress class"""

        # Initialize members of the class
        if street is not APIHelper.SKIP:
            self.street = street 
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if zip is not APIHelper.SKIP:
            self.zip = zip 
        if country is not APIHelper.SKIP:
            self.country = country 

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
        street = dictionary.get("street") if "street" in dictionary.keys() else APIHelper.SKIP
        line_2 = dictionary.get("line2") if "line2" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("city") if "city" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get("state") if "state" in dictionary.keys() else APIHelper.SKIP
        zip = dictionary.get("zip") if "zip" in dictionary.keys() else APIHelper.SKIP
        country = dictionary.get("country") if "country" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(street,
                   line_2,
                   city,
                   state,
                   zip,
                   country)
