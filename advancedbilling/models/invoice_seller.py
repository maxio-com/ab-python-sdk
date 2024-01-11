# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress


class InvoiceSeller(object):

    """Implementation of the 'Invoice Seller' model.

    Information about the seller (merchant) listed on the masthead of the
    invoice.

    Attributes:
        name (str): TODO: type description here.
        address (InvoiceAddress): TODO: type description here.
        phone (str): TODO: type description here.
        logo_url (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "address": 'address',
        "phone": 'phone',
        "logo_url": 'logo_url'
    }

    _optionals = [
        'name',
        'address',
        'phone',
        'logo_url',
    ]

    _nullables = [
        'logo_url',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 logo_url=APIHelper.SKIP):
        """Constructor for the InvoiceSeller class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if address is not APIHelper.SKIP:
            self.address = address 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if logo_url is not APIHelper.SKIP:
            self.logo_url = logo_url 

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
        logo_url = dictionary.get("logo_url") if "logo_url" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   address,
                   phone,
                   logo_url)

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
