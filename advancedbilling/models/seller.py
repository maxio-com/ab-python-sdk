# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress


class Seller(object):

    """Implementation of the 'Seller' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        address (InvoiceAddress): TODO: type description here.
        phone (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "address": 'address',
        "phone": 'phone'
    }

    _optionals = [
        'name',
        'address',
        'phone',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 phone=APIHelper.SKIP):
        """Constructor for the Seller class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if address is not APIHelper.SKIP:
            self.address = address 
        if phone is not APIHelper.SKIP:
            self.phone = phone 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        address = InvoiceAddress.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   address,
                   phone)
